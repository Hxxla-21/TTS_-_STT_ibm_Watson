import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api = IAMAuthenticator('G5cSyxVG132iTdfF9NZFeR8w8c2qBqNRvTR5UoSpKw31')

speech2text= SpeechToTextV1(authenticator=api)


speech2text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/d1e34d94-6127-41fd-9b22-27641ca24bf8')

with open("welcome.mp3","rb") as audiofile:
    
    result=speech2text.recognize(
        audio=audiofile, content_type="audio/mp3"
    ).get_result()
    file=open("myfile.txt","w")
    str_result=repr(result)
    file.write("the result= "+str_result)
    file.close()
