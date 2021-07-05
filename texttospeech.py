# -*- coding: utf-8 -*-
#!/usr/bin/python3

from gtts import gTTS
# pip install gtts
from playsound import playsound
# pip install playsound

# Instagram: @oicarosalles

audio = 'speech_pt.mp3'
language = 'pt-br'

sp = gTTS(text="Siga oicarosalles no Instagram e receba várias dicas sobre programação!",
          lang=language, slow=False)

sp.save(audio)
playsound(audio)
