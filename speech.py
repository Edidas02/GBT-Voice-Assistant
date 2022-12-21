import speech_recognition as sr
from pyChatGPT import ChatGPT
import tokens
#from chatgpt_wrapper import ChatGPT

# initialize the recognizer
r = sr.Recognizer()

# session token for chatgpt
session_token = tokens.session_id
#start a remote chatgpt api
api = ChatGPT(session_token)
#api = ChatGPT()

# read in audio from the microphone
with sr.Microphone() as source:
    print("Please say your question: ")
    audio = r.listen(source)
try:
    print("This is the prompt you said: " + r.recognize_google(audio))
    prompt = r.recognize_google(audio)
except sr.UnknownValueError:
    print("I'm sorry but I could not understand the audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

response = api.send_message(prompt)
print("This is ChatGPT's response")
print(response['message'])
api.close()


