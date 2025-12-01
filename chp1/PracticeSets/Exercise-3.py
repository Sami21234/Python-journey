# 3. Install an external module and use it to perform an operation of your interest. 
# Downloaded the external module which will speak the text which will be written.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hii Sami")
engine.runAndWait()