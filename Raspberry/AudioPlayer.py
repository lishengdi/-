from pygame import mixer
import time
mixer.init()
mixer.music.load('result.mp3')
mixer.music.play()
time.sleep(5)
mixer.music.stop()

