# pip install pyttsx3
import pyttsx3

engine = pyttsx3.init()

# Get List of Voices
voices = engine.getProperty('voices')

# for v in voices:
#     print( v )

# SET Male Voice
# <Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
# name=Microsoft David Desktop - English (United States)
engine.setProperty('voice', voices[0].id)

engine.say( 'Hello World!' )

# SET female Voice
# <Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# name=Microsoft Zira Desktop - English (United States)

engine.setProperty('voice', voices[1].id)

name = input( 'Enter Name:' )
engine.say( 'Hello' + name  )

engine.runAndWait()