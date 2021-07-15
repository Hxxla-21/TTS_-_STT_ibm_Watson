import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api = IAMAuthenticator('UtMD_Rm1yhk7T_iZVzk-ryDHbSTC270mW2LMigHXhOmJ')

text2speech= TextToSpeechV1(authenticator=api)


text2speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/f14a0b3d-3272-47dd-9e49-f78f55bc4a6d')

with open("welcome.mp3","wb") as audiofile:
        audiofile.write(
            text2speech.synthesize("Hello, My Name is Hala. I'm a software engineering from a University of jeddah, thank you ",accept="audio/mp3").get_result().content
        )
