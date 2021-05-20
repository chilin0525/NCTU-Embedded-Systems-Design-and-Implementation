from gtts import gTTS
import os

tts = gTTS(text='你好', lang='zh-TW')
tts.save('hello.mp3')

os.system('omxplayer -o local -p hello.mp3 > /dev/null 2>&1')
