# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 01:27:54 2018

@author: Taha Anwar
"""

import threading
import random        
import numpy as np
from multiprocessing import Manager, Value
from ctypes import c_char_p
import os

import cv2
#import time
import sys
forloop =False
#cap = cv2.VideoCapture(0)
#cap1 = cv2.VideoCapture(1)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\Dell\Downloads\api-key.json'

face_cascade = cv2.CascadeClassifier(r'C:\Users\Dell\.spyder-py3\haarcascade_frontalface_default.xml')
newx,newy=50,50
initialx1=210
initialx2=642
initialy1=170
initialy2=170
exitflag = False
import multiprocessing
from pynput.keyboard import Key, Controller
from pynput.mouse import  Controller as cc
from pynput.mouse import  Button
import pynput
print('Initializing..')
fbpost='no posts yet'
from tkinter import * 
from PIL import  ImageTk
import PIL.Image


import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import random

from playsound import playsound
import webbrowser
from selenium import webdriver
from subprocess import Popen, check_call

from bs4 import BeautifulSoup
import requests

import dialogflow 
import uuid
text='how old are you'
language_code = 'en-US'
session_id=  str(uuid.uuid4())
project_id ='testrobot-196008'
from google.cloud import translate


try:
  translate_client = translate.Client()
except:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\Dell\Downloads\api-key.json'
    translate_client = translate.Client()


from google.cloud import vision
from google.cloud.vision import types
import io
from skimage.feature import hog
import cv2
import time
import matplotlib.pyplot as plt

#try:
#    cap.release()
#except:
#   pass
#try:
#    cap1.release()
#except:
#   pass 


    
defaultargs = ["I didn't get that. Can you say it again?",
 "missed what you said. Say it again? ", "Sorry, could you say that again?"
 ,"Sorry, can you say that again?" , "Can you say that again?" , "Sorry, I didn't get that."
 ,"Sorry, what was that?","One more time, please say it again?"
 ,"What was that again?", "Say that again?", "I didn't get that."]   

imagesubtract=['finger','hand','hair','room','fun','ceiling','interior design','house','jaw','forehead',
  'selfie','chin','arm'] 

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
impclass = ['Z0LcW','lr_dct_sf_sen vk_txt','PNlCoe','cwcot','Y0NH2b CLPzrc']


myprograms={
   "torrent":r"C:\Users\Dell\AppData\Roaming\uTorrent\uTorrent.exe",
   "notepad":r'C:\Users\Dell\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Notepad',
  "browser":r"C:\Program Files\Mozilla Firefox\firefox.exe",
 "photoshop": r"C:\Program Files\Adobe\Adobe Photoshop CS5\Photoshop.exe",
"microsoft word":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007"}


languages =   { "Afrikaans": "af","Albanian": "sq" ,  "Arabic":"ar", "Bengali":"bn", 
     "Chinese":"zh-cn" ,  "Danish":"da",  "Dutch":"nl","English":  "en",
     "Finnish":"fi" ,"French":"fr" ,   "German":"de" ,"Greek" : "el",
   "Hindi": "hi"  , "Hungarian":"hu" ,"Indonesian": "id" ,
   "Italian":"it" , "Japanese":"ja" ,
  "Korean" : "ko" , "Latin" : "la" ,"Latvian"  :"lv" ,
  "Norwegian":"no" ,	"Polish": "pl" ,
"Portuguese":"pt" ,"Romanian":"ro" ,"Russian":"ru","Spanish": "es" ,
 "Swedish":"sv" , "Tamil": "ta" , "Thai":"th" ,"Turkish":"tr" ,
 "Ukrainian":"uk","Vietnamese":"vi" }


def maincall(fstring,ystring,nstring,statecam,speakflag,listenflag):
    def speak(audioString):
        if speakflag.value == 'true':
            
            try:
    
                r1 = random.randint(1,10000000)
                r2 = random.randint(1,10000000)
                randfile = str(r2)+"randomtext"+str(r1) +".mp3"
                #print(audioString)
                fstring.value = audioString
                tts = gTTS(text=audioString, lang='en',slow=False)
                tts.save(randfile)
                playsound(randfile)
                os.remove(randfile)
    
            except:
               #print(audioString)
               fstring.value = audioString
        else:
            #print('false not true')
            fstring.value = audioString
            
    def takeimages():
         try:       
                statecam.value= 'negative'
                time.sleep(2)
                t=time.time()
                cap1 = cv2.VideoCapture(0)
                nstring.value = 'capturing'
                while (True):
                   if cap1.isOpened(): 
                        ret ,frame = cap1.read()   
                        if ret:
                           cv2.imshow("img",frame)
                           if cv2.waitKey(1)  & 0xFF ==ord('w'):
                                break
                           if time.time() - t > 5:
                               cv2.imwrite('imageanalysis.jpeg',frame)
                               print('saved')
                               break
                        else:
                             cap1.open()
                cap1.release()
                cv2.destroyAllWindows()  
                client = vision.ImageAnnotatorClient()
                with io.open('imageanalysis.jpeg', 'rb') as image_file:
                     content = image_file.read()
                image = types.Image(content=content)
                
                # Performs label detection on the image file
                response = client.label_detection(image=image)
                labels = response.label_annotations
                aa =[] 
                for label in labels:
                    aa.append(label.description)
            
                print('Labels:')
                for label in labels:
                    print(label.description, label.score)
                statecam.value= 'positive'    
                return aa    
         except Exception as e:
            print(e)

    def detect_text():
        try:
            statecam.value= 'negative'
            time.sleep(2)
            t=time.time()
            cap1 = cv2.VideoCapture(0)
            #print('started reading')
            nstring.value= 'Started Reading..'
            while (True):
                if cap1.isOpened():
                    
                    ret ,frame = cap1.read()   
                    if ret:
                       cv2.imshow("img",frame)
                       if cv2.waitKey(1)  & 0xFF ==ord('w'):
                            break
                       if time.time() - t > 8:
                           cv2.imwrite('textimageanalysis.jpeg',frame)
                           #print('almost done')
                           nstring.value= 'almost done..'
                           break
                    else:
                        print('not ret')
                else:
                   print('opened cap') 
                   cap1.open()
            cap1.release()
            cv2.destroyAllWindows()  
            client = vision.ImageAnnotatorClient()
    
            with io.open('textimageanalysis.jpeg', 'rb') as image_file:
                content = image_file.read()
    
            image = types.Image(content=content)
    
            response = client.text_detection(image=image)
            texts = response.text_annotations
            #print('Texts:')
            nstring.value= 'I Understand following from pic:'     
            #print(texts)
            finaltext =''
            for text in texts:
                finaltext += text.description + ' '
            statecam.value= 'positive'    
            return finaltext  
        except Exception as e :
             print(e)


   

    def recordAudio( project_id, session_id, language_code):
        try:
            # Record Audio
            r = sr.Recognizer()
            with sr.Microphone() as source:
                #print("...")
                nstring.value= 'calibrating...'
                r.adjust_for_ambient_noise(source, duration=2) 
                #print("Alright Speak....")
                nstring.value= "Alright Speak...."
                audio = r.listen(source)
                with open("newrecording.wav", "wb") as f:
                     f.write(audio.get_wav_data())
            # Speech recognition using Google Speech Recognition
            nstring.value= "thinking what you said: "
            audio_file_path = 'newrecording.wav'
            data = ""
            session_client = dialogflow.SessionsClient()

            # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
            audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
            sample_rate_hertz = 44100

            session = session_client.session_path(project_id, session_id)
           # print('Session path: {}\n'.format(session))

            def request_generator(audio_config, audio_file_path):
                query_input = dialogflow.types.QueryInput(audio_config=audio_config)

                # The first request contains the configuration.
                yield dialogflow.types.StreamingDetectIntentRequest(
                    session=session, query_input=query_input)

                # Here we are reading small chunks of audio data from a local
                # audio file.  In practice these chunks should come from
                # an audio input device.
                with open(audio_file_path, 'rb') as audio_file:
                    while True:
                        chunk = audio_file.read(4096)
                        if not chunk:
                            break
                        # The later requests contains audio data.
                        yield dialogflow.types.StreamingDetectIntentRequest(
                            input_audio=chunk)

            audio_config = dialogflow.types.InputAudioConfig(
                audio_encoding=audio_encoding, language_code=language_code,
                sample_rate_hertz=sample_rate_hertz)

            requests = request_generator(audio_config, audio_file_path)
            responses = session_client.streaming_detect_intent(requests)

            for response in responses:
                pass

            query_result = response.query_result
            data = query_result.query_text
            #print('you said: ' + str(data))
            nstring.value= "I'm done"
            return data, query_result.fulfillment_text
        except:
            #print('couldnt hear you..')
            nstring.value= 'couldnt hear you..'

    def frieza(data,answerdialog):
        global myprograms
        global imagesubtract

        if "what is your name" in data:
            speak("My name is Frieza.")

        elif "what time is it" in data:
            speak(ctime())
            
            
        elif "set post to" in data and 'set' in  data.split(' ')[0].lower():
            global fbpost
            fbpost = data.replace('set post to','')
            speak('post saved')
            #print (newdata)     
        elif 'post to facebook' in data.lower() and 'post' in  data.split(' ')[0].lower():
           try:
               
                keyboard = Controller()
                mouse = cc()
                speak('Posting to facebook')
                keyboard.press(Key.cmd)
             
                keyboard.press('m')
                keyboard.release('m')
                keyboard.release(Key.cmd)
                
                time.sleep(1)
                
                
                webbrowser.open('http://www.facebook.com')
                
                time.sleep(17)  
                print('doing')
                mouse.position = (484, 204)
                mouse.click(pynput.mouse.Button.left, 2)
                keyboard.type(fbpost)
                time.sleep(3)
                mouse.position = (721, 380)
                time.sleep(4)
                mouse.click(pynput.mouse.Button.left, 1)
                print('completed')
           except Exception as e:
                print(e)

        elif 'translate' in  data.split(' ')[0]  and 'this' not in data.split(' ')[1].lower():
             if data.split(' ')[-1] in languages:
                 extraction =data.split(' ',1)[1]
                 extraction = extraction.split(' ')[:-2]
                 extraction = ' '.join(extraction)
                 translation = translate_client.translate(extraction,target_language=languages[data.split(' ')[-1]])

                 #print(extraction) 
                 
                 speak(u'Translation: {}'.format(translation['translatedText']))
                 
             else:
                 speak('sorry i dont know any language named ' +  str(data.split(' ')[-1]))

        #Launch programs
        elif 'launch' in  data.split(' ')[0].lower()  or 'open' in data.split(' ')[0].lower():
             if  data.split(' ', 1)[1].lower()  in  myprograms:
                 speak("Opening up " + str( data.split(' ', 1)[1]) )
                 os.startfile(myprograms[data.split(' ', 1)[1].lower()])
             else:
                 speak('did not found any program named: ' + str( data.split(' ', 1)[1]))






        #perform google search
        elif ('search' in  data.split(' ')[0] and 'for' in data.split(' ')[1]) or 'Google' in data.split(' ')[0]:
              if 'for' in data.split(' ')[1]:
                  query =data.split(' ', 2)[2]
                  #print (query)
              elif 'Google' in data.split(' ')[0]:
                  query =data.split(' ', 1)[1]
                  #print (query)
              query2 = query.replace(" ","+")
              browserurl = 'https://www.google.com/search?q='+query2
              
              #driver = webdriver.Firefox()
              #driver.get(browserurl)
              speak('searching for ' + query)
              webbrowser.open(browserurl)
        #catch images     
        elif  data.lower() == 'what do you see'  or 'what  am I holding' in data.lower():
            keyboard = Controller()
            mouse = cc()
            keyboard.press(Key.cmd)
         
            keyboard.press('m')
            keyboard.release('m')
            keyboard.release(Key.cmd)
                
            olabels = takeimages()
            l3 = [x for x in olabels if x not in imagesubtract]
            keyboard.press(Key.cmd)
            keyboard.press(Key.shift)
         
            keyboard.press('m')
            keyboard.release('m')
            keyboard.release(Key.cmd)
            keyboard.release(Key.shift)

            if len(l3) < 2:
                speak(", ".join(olabels))
            else:
                 speak(", ".join(l3))

        elif  data.lower() == 'read this'  or 'what is written here' in data.lower():
            keyboard = Controller()
            mouse = cc()
            keyboard.press(Key.cmd)
         
            keyboard.press('m')
            keyboard.release('m')
            keyboard.release(Key.cmd)
            finatext = detect_text()

            if finatext is not None:
                keyboard.press(Key.cmd)
                keyboard.press(Key.shift)
             
                keyboard.press('m')
                time.sleep(0.5)
                keyboard.release('m')
                keyboard.release(Key.cmd)
                keyboard.release(Key.shift)
                if len(finatext.split(' ')) < 35:
                            speak(finatext)
                else:
                   fstring.value =finatext
            else:
                speak('Sorry I did not detected anything')


    
        else:
            if len(data) > 2:
                if answerdialog in defaultargs:
                    
                    query=data
                    query = query.replace(" ","+")
                    url = 'https://www.google.com/search?q='+query
                    r  = requests.get(url,headers=headers).text
                    soup = BeautifulSoup(r,'html.parser')
                           
                    for x in impclass:
                        if impclass[-1] == x:
                           getvalue=soup.find('span',class_=x) 
                        elif impclass[-2] == x:
                           getvalue=soup.find('span',class_=x)                            
                        else:
                           getvalue=soup.find('div',class_=x) 
                           
                        if getvalue is not None:
                           if len(getvalue.text.split(' ')) < 35:
                                speak(getvalue.text)
                           else:
                               #print(getvalue.text)
                               fstring.value=getvalue.text
                           break
                        if impclass[-1] == x:
                           getvaluec1=soup.find('div',class_="vk_ans vk_bk")#currency first
                           getvaluec2=soup.find('div',class_="vk_sh vk_gy")#currency second
                           if getvaluec1 is not None and getvaluec2 is not None:
                                final = getvaluec2.text + ' '+ getvaluec1.text
                                speak(final)
                         
                           else:
                                speak(answerdialog)
                else:
                      speak(answerdialog)
    def detect_intent_texts(project_id, session_id, text, language_code):
        """Returns the result of detect intent with texts as inputs.
    
        Using the same `session_id` between requests allows continuation
        of the conversaion."""
        nstring.value='thinking'
        session_client = dialogflow.SessionsClient()
        
        session = session_client.session_path(project_id, session_id)
        #print('Session path: {}\n'.format(session))
    
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
    
        query_input = dialogflow.types.QueryInput(text=text_input)
    
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        nstring.value='done'
        return response.query_result.query_text,response.query_result.fulfillment_text
        
          
    
    
    
    
    print('maincall running')
    time.sleep(1)
    speak("What can i do for you sir.")
    tempholder='none'
    while 1:
        try:
           if listenflag.value == 'true':

                
               data , answerdialog= recordAudio(project_id, session_id, language_code)
               ystring.value = data
               if "quit now" in data or 'finish proccess now' in data:
                speak("ok, bye bye Sir.")
                break
           
               frieza(data,answerdialog)
           else:
               if tempholder != ystring.value:
                   nstring.value = 'type: '
                   data2,answerdialog2=detect_intent_texts(project_id, session_id, ystring.value, language_code)
                   tempholder = ystring.value
                   
                   if "quit now" in data2 or 'finish proccess now' in data2:
                        speak("ok, bye bye Sir.")
                        break
                           
                   frieza(data2,answerdialog2)
           
            
        except Exception as e:
             print('main',e)
            
    speak("Ended")    
    




    
def second(fsetter,ysetter,notice,state,speakflag,listenflag):
   


    image0 =PIL.Image.open(r"C:\Users\Dell\.spyder-py3\output0.png")
    image1 =PIL.Image.open(r"C:\Users\Dell\.spyder-py3\output1.png")
    image2 = PIL.Image.open(r"C:\Users\Dell\.spyder-py3\output2.png")
    image3 = PIL.Image.open(r"C:\Users\Dell\.spyder-py3\output3.png")
    image4 = PIL.Image.open(r"C:\Users\Dell\.spyder-py3\output4.png")
    image5 = PIL.Image.open(r"C:\Users\Dell\.spyder-py3\finaleyebrows.png")
    print('started')
   # from tkinter import * 
    #try:
    #    root= Tk()
    #except:
    #tt= Tk()
    #tt.title('Running')
    root = Toplevel()

    canvas = Canvas(root,width=1000,height=500,bd=0,highlightthickness=0) # bd= border

    mimage0 = ImageTk.PhotoImage(image0)
    mimage1 = ImageTk.PhotoImage(image1)
    mimage2 = ImageTk.PhotoImage(image2)
    mimage3 = ImageTk.PhotoImage(image3)
    mimage4 = ImageTk.PhotoImage(image4)
    eyebrow = ImageTk.PhotoImage(image5)
    animeeye = PhotoImage(file='animeeye.gif')
    animeeye = animeeye.zoom(2,2)
    images = [mimage0,mimage1,mimage2,mimage3,mimage4]                    

    root.title("Frieza")
    #root.wm_attributes("-topmost",2) 


    def moveend(eventxx):
        global forloop
        global exitflag
        forloop = True
        exitflag = True

        root.destroy()



    canvas.grid(row=0,column=0,columnspan=4)
    #canvas.pack()


    root.bind("<End>",moveend)


    can1=canvas.create_image(initialx1,initialy1,anchor=NW,image=animeeye)  
    can2=canvas.create_image(initialx2,initialy2,anchor=NW,image=animeeye)     

    obj=canvas.create_image(0,0,anchor=NW,image=mimage0) 

    can3=canvas.create_image(0,0,anchor=NW,image=eyebrow) 

    #entrybox = Entry(root,fg='blue')
    #entrybox.grid(row=1,column=1)
    t1= 'You said: ' +'when were you born'
    t2= 'Frieza: '+'i was born in clombia but i am living here for two yers now i was born in clombia but i am living here\
    for two yers now i was born in clombia but i am living here for two yers now '
    notes = 'Speak, Im listning...'
    n1= Message(root,text=notes ,fg='red',font="Ariel 9 italic",width=300)
    n1.grid(row=1,column=0 )
    w1= Message(root,text=t1 ,fg='blue',font="Ariel 12 italic",width=900)
    w1.grid(row=2,column=0)
    varspeak = IntVar()
    varlisten = IntVar()
     
    
    def textentry(dfaultparam):
         ysetter.value = entrybox.get()
         entrybox.delete(0, END)
         
         
    check1 = Checkbutton(root, text="Do not Speak", variable=varspeak)
    check1.grid(row=2,column=3)
    
    w2 = Message(root, text=t2, width=900,fg='green',font="Ariel 13 bold")
    #l1= Label(root,text=t2,fg='green',font="Ariel 16 bold")
    w2.grid(row=4,column=0)
    check2 = Checkbutton(root, text="Typing On", variable=varlisten)
    check2.grid(row=4,column=3)
    
    indicatorlabel= Label(root,text='Type here: ',fg='orange',font="Ariel 10 bold")
    indicatorlabel.grid(row=5,column=0)
    entrybox= Entry(root,font="Ariel 12 italic",width=100)
    entrybox.grid(row=6,column=0)
    entrybox.bind("<Return>",textentry)
    entrybox.config(state=DISABLED)

    
         
        

    def pinter():
        global exitflag, newx, newy, initialx1, initialx2, initialy1, initialy2
        cap = cv2.VideoCapture(0)
        ytemp,ftemp,ntemp='none','none','none'
        thestate= 'notchanged'

        while 1:
            if ytemp != ysetter.value:
                w1.configure(text = ysetter.value)
                ytemp = ysetter.value
            if ftemp != fsetter.value:
                w2.configure(text = fsetter.value)
                ftemp = fsetter.value 
            if ntemp != notice.value:
                n1.configure(text = notice.value)
                ntemp = notice.value     
                
            
            if varspeak.get() == 1:
                speakflag.value= 'false'
                
            else:
                speakflag.value= 'true'
                
            
            if varlisten.get() == 1 :
                listenflag.value = 'false'
                entrybox.config(state='normal')
                
            else:
                listenflag.value = 'true'
                entrybox.config(state=DISABLED)
                
            
            if state.value == 'positive':
                if thestate == 'changed':
                   cap = cv2.VideoCapture(0)
                   time.sleep(1)
                   thestate = 'notchanged'
                else:
                    pass
                ret, img = cap.read()
    
               
    
                if ret:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    #using the try block here because faces  gives '()' when there are no faces in front and so there is an error
                    try:
                        x,y,w,h = faces[0]
    
    
    
                        newx=np.interp(x,[0,480],[0,90])
                        newy=np.interp(y,[0,480],[0,50])  
                        newx = newx -45
                        newy = newy -25
    
                        finalx1= initialx1-newx
                        finalx2= initialx2-newx
                        finaly1= initialy1+newy
                        finaly2= initialy2+newy
    
    
    
                        canvas.coords(can1, (finalx1,finaly1))
                        canvas.coords(can2, (finalx2,finaly2))
    
                        root.update()   
    
                    except:
                        pass
                    if exitflag:
                        cap.release()

                        break
                    
            else:
                 thestate= 'changed'
                 cap.release()      

    def animator():

        while 1:

            global forloop
            r=random.randrange(5)
            for i in images:
                  canvas.itemconfig(obj, image = i)
                  #print(i)              
                  root.update()
                  time.sleep(0.15)
            time.sleep(r)
            if forloop == True:
                break
                print('executed')

    t1= threading.Thread(target=animator)
    t2= threading.Thread(target=pinter)

    t1.start()
    t2.start()


    root.mainloop()
    
if __name__ == '__main__':
    manager = Manager()
    string1 = manager.Value(c_char_p, "")
    string2 = manager.Value(c_char_p, "")
    string3 = manager.Value(c_char_p, "")
    string4 = manager.Value(c_char_p, "positive")
    speakflag = manager.Value(c_char_p, "true")
    listenflag = manager.Value(c_char_p, "true")
    

    mainprocess = multiprocessing.Process(target=maincall, args=(string1,string2,string3,string4,speakflag,listenflag))
    mainprocess2 = multiprocessing.Process(target=second,args=(string1,string2,string3,string4,speakflag,listenflag))
    mainprocess.start()
    mainprocess2.start()        
    mainprocess.join()
    mainprocess2.join()