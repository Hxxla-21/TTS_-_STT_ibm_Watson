import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api = IAMAuthenticator('5ryInlRr2O74-b_VOUeJkrpat653l3kLoQWeNjFgAa4I')

speech2text= SpeechToTextV1(authenticator=api)


speech2text.set_service_url('https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/182a22de-7481-4b7f-beb5-5e29c3c6dd0d')

with open("welcome.mp3","rb") as audiofile:
    
    result=speech2text.recognize(
        audio=audiofile, content_type="audio/mp3"
    ).get_result()
    file=open("myfile.txt","w")
    str_result=repr(result)
    file.write("the result= "+str_result)
    file.close()
