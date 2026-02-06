import speech_recognition as sr
import pyttsx3 

import requests,pyaudio
from datetime import datetime
import webbrowser
import requests
#ip api.com
#corpus collection of data elements


greet=["hi","hello","hey","hi there","hey there",]
datetime_msgs=["what's the date","date","tell me date","today's date"]
time_msgs=["tell me time","what's the time","today's time","current time"]
news_intent=["tell me news","latest news"]
chat=True

engine=pyttsx3.init()
engine.setProperty("rate",170)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=rec.listen(source)
    try:
        query = rec.recognize_google(audio)
        print("Your query :",query)
        return query.lower()
    except BaseException as ex:
        print("Can't catch that....")
        print("Exception:",ex)
        return ''



#NEWS_API_KEY =  751838845890408d92385180eabc7eeb
'''
response=requests.get(url)
response.json()
data=response.json()
#pip install pipwin
#pipwin install pyaudio
a=data["articles]
a[0]["titles"]
'''
def get_location():
    response=requests.get("http://ip-api.com/json/")
    data=response.json()
    city=data.get("city","Unknown location")
    country=data.get("country","Unknown location")
    return country,city
def get_weather():
    WEATHER_API_KEY="263b40b42de7bc7f85195ff88d022a14"
    country,city=get_location()
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response=requests.get(url)
    data=response.json()
    print(data)
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    return f"Weather in {city}:\nTemperature: {temp}°C\nCondition: {desc}\nHumidity: {humidity}%"

def get_news():
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=751838845890408d92385180eabc7eeb"
    #url="https://newsapi.org/v2/everything?q=apple&from=2026-01-30&to=2026-01-30&sortBy=popularity&apiKey=751838845890408d92385180eabc7eeb"
    response=requests.get(url)
    data=response.json()
    articles=data['articles']
    total_articles=len(articles)
    for i in range(total_articles):
        print("Headline ",i+1,articles[i]['title'])

while(chat):
    #ch=int(input("Enter your choice: \n1-> Microphone \n2->text message"))
    #if(ch==1):
    msg=listen()
    #if(ch==2):
     #   msg=input("Enter you message : ").lower()
    if(msg in greet):
        print("Hello how are you")
    elif msg in datetime_msgs:
        print(datetime.now().date())
    elif("open" in msg):
        site=msg.split("open ")[-1]
        url=f"https://www.{site}.com"
        webbrowser.open(url)
        print(f"Opening {site}...")
    elif("location" in msg):
        print("Your country is :",get_location()[0])
        print("Your city is :",get_location()[1])
    elif("weather" in msg):
        print(get_weather())
    elif("news" in msg):
        get_news()
    elif msg in time_msgs:
        current_time=datetime.now().time()
        print(current_time.strftime("%I:%M:%S"))
    elif("calculate" in msg):
        op=msg.split("calculate ")[-1]
        print(eval(op))
    elif("ip" in msg):
         query=msg.split(" ")[-1]
         url=f"http://ip-api.com/json/{query}"
         response=requests.get(url)
         data=response.json()
         print(data)
    elif(msg=="bye" or msg=="exit" or msg=="stop"):
        chat=False
    else:
        print("I can't understand")
  
