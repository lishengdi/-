#include <Adafruit_Fingerprint.h>
#include<Servo.h>
int pos=0;
Servo myLock;
// On Leonardo/Micro or others with hardware serial, use those! #0 is green wire, #1 is white
// uncomment this line:
// #define mySerial Serial1

// For UNO and others without hardware serial, we must use software serial...
// pin #2 is IN from sensor (GREEN wire)
// pin #3 is OUT from arduino  (WHITE wire)
// comment these two lines if using hardware serial
SoftwareSerial mySerial(2, 3); // RX,TX(UNO)  //指纹模拟串口
SoftwareSerial postMan(10, 11); //向树莓派传递信息


Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

uint8_t id;
uint8_t tryTime;

void lightOn();
void setup()  
{
  tryTime=0;
  pinMode(13,INPUT);   //监听树莓派开门请求
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(4,INPUT);
  pinMode(12,OUTPUT); //向树莓派发出中断触发信号
  Serial.begin(9600);
  while (!Serial);  // For Yun/Leo/Micro/Zero/...
  delay(100);
//  Serial.println("\n\nAdafruit Fingerprint sensor enrollment");

  // set the data rate for the sensor serial port
  finger.begin(57600);
  postMan.begin(4800);
  mySerial.println("hello");
  if (finger.verifyPassword()) {
    Serial.println("Found fingerprint sensor!");
  } else {
    Serial.println("Did not find fingerprint sensor :(");
    while (1) { delay(1); }
  }
  myLock.attach(5);  //舵机pwm接口

  for (pos=90;pos>=0;--pos){  //预先上锁
    myLock.write(pos);
    delay(5);
  }
  digitalWrite(12,LOW);
  
}

void loop()                     // run over and over again
{
  int val=Serial.read();   //蓝牙开门
  if (val=='t'){
    digitalWrite(12,HIGH);
    delay(100);
    digitalWrite(12,LOW);
    postMan.println("BLE");
    
    openDoor();
  }else if(val=='f'){
    closeDoor();
  }
  
  if(digitalRead(13)==HIGH){   //树莓派人脸识别开门
    openDoor();
  }
 
  if(tryTime>3){
    alarm();
  }
  if(digitalRead(4)==HIGH)
      {
        getFingerprintIDez();
        delay(500);
      }

  delay(300);           
}


// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK) {
     return -1;
  }
  
 

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK) {
    return -1;
  }

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK){
    tryTime++;
    return -1;
  }
  
  // found a match!
  Serial.print("Found ID #"); Serial.print(finger.fingerID); 
  Serial.print(" with confidence of "); Serial.println(finger.confidence);
  
   digitalWrite(12,HIGH);   //向树莓派报告身份
    delay(100);
    digitalWrite(12,LOW);
    postMan.println(finger.fingerID);
    
  openDoor();
  tryTime=0;
  return finger.fingerID; 
}



void alarm(){
//  Serial.println("startAlarm");
  digitalWrite(12,HIGH);   //向树莓派报告身份
    delay(100);
    digitalWrite(12,LOW);
    postMan.println("Alarm");
    
  tryTime=0;
      for(int i=200;i<=800;i++)                    //用循环的方式将频率从200HZ 增加到800HZ
    {
      tone(6,i);                            //在四号端口输出频率
    delay(5);                              //该频率维持5毫秒   
    }
    delay(1500);                            //最高频率下维持4秒钟
    for(int i=800;i>=200;i--)
    {
      tone(6,i);
    delay(10);
    }
    noTone(6);
}

void openDoor(){
  for(pos==0;pos<=90;++pos){
     myLock.write(pos);
     delay(5);
  }
  if(analogRead(0)>=300){
    lightOn();
    delay(1000);
   }else{
     delay(4000);
    }
  for (pos=90;pos>=0;--pos){    //自动关门
    myLock.write(pos);
    delay(5);
  }   
}
void closeDoor(){
  for (pos=90;pos>=0;--pos){
    myLock.write(pos);
    delay(5);
  }
}

void lightOn(){
  digitalWrite(7,HIGH);
      delay(3000); 
      digitalWrite(7,LOW);
}
