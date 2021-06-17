#include<Servo.h>
int pos=0;
Servo myLock;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  myLock.attach(5);
    for (pos=90;pos>=0;--pos){
    myLock.write(pos);
    delay(5);
  }
}

void loop() {
//  myLock.write(0);
//  delay(2000);
//  
//  for (pos=0;pos<=90;++pos){
//    myLock.write(pos);
//    delay(5);
//  }
//  delay(4000);
////  for(pos=0;pos>=-180;--pos){
////    myLock.write(pos);
////    delay(5);
////  }
if(Serial.read()=='k')
open();

}
void open(){
  for(pos==0;pos<=90;++pos){
     myLock.write(pos);
     delay(5);
  }
   
delay(2000);
   for (pos=90;pos>=0;--pos){
    myLock.write(pos);
    delay(5);
  }

}
