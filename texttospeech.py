from gtts import gTTS

import os
import sys
import time

mytext = 'welcome my lord'

language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("output.mp3")

os.system("start output.mp3")
  
