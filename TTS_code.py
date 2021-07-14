import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api = IAMAuthenticator('9_8pHCLe5Ief6hrWv1QPiWncPmZrnWXoMUd5FH2kA410')

text2speech= TextToSpeechV1(authenticator=api)


text2speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/ce312d68-67a2-4bab-a06c-7c5dc4200d42')

with open("welcome.mp3","wb") as audiofile:
        audiofile.write(
            text2speech.synthesize("Hello, My Name is Hala. I'm a software engineering from a University of jeddah ",accept="audio/mp3").get_result().content
        )