import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener= sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
  engine.say(text)
  engine.runAndWait()
def get_info():

  try:
    with sr.Microphone() as source:
      print('lisining...')
      voice=listener.listen(source)
      info=listener.recognize_google(voice)
      print(info)
      return info.lower()
  except:
    pass
def send_email(receiver,subject,message):


  server= smtplib.SMTP('smtp.gmail.com',587)
  server.starttls()
  server.login('your email id','Email passward')
  email=EmailMessage()
  email['From']='your email'
  email['To']=receiver
  email['Subject']=subject
  email.set_content(message)
  server.send_message(email)

email_list={
  'reciver name':'reciver email id'
  'reciver name':'reciver email id'
  'reciver name':'reciver email id'
  'reciver name':'reciver email id'
  'reciver name':'reciver email id'
  'reciver name':'reciver email id'
}
def get_email_info():
  talk('To whome would you like to send your email')
  name=get_info()
  receiver=email_list[name]
  print(receiver)
  talk('What is your email subject')
  subject=get_info()
  talk('What is the text')
  message=get_info()
  send_email(receiver,subject,message)

get_email_info()  

