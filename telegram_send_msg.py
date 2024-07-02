import time
#import schedule
import requests
import telegram
import os
data=requests.get("https://msbauthentication.com/autocontrol/api/readtelegram.php")
data=[{"api_token":"1330463965:AAGqzLOiUGXP8HV6d0Ssq8uda9eCKJ-dWRQ","chat_id":"-1001151822648","purpose":"alerts","remark":None,"purpose_id":"2"},{"api_token":"1278809595:AAFTuDNeHk0tDAH05HBrXPy4ZtIc3dwB_3M","chat_id":"-1001407170402","purpose":"orders","remark":None,"purpose_id":"1"}]

def vardec(mobile_num1):
    global mobile_num
    mobile_num=mobile_num1

def telegram_bot_sendtext(bot_message,purpose_id):
    try:
        purpose_id = int(purpose_id)
        #for i in range(purpose_id):
        if purpose_id == 1:
            bot=telegram.Bot(token=data[0]["api_token"])
            chat_id=data[0]["chat_id"].split(',')
            print(chat_id)
            for i in range(0,len(chat_id)):
                bot_message="MI-->"+str(mobile_num)+":"+bot_message
                bot.send_message(chat_id=chat_id[i],text=bot_message)
        
        if purpose_id == 2:
            bot=telegram.Bot(token=data[1]["api_token"])
            chat_id=data[1]["chat_id"].split(',')
            print(chat_id)
            for i in range(0,len(chat_id)):
                bot_message="MI-->"+str(mobile_num)+":"+bot_message
                bot.send_message(chat_id=chat_id[i],text=bot_message)
    except Exception as e:
        print(e)
        pass


def telegram_bot_sendimage(image_url,purpose_id,phone,msg,maindata,campaignid):
    try:
        purpose_id = int(purpose_id)
        #for i in range(purpose_id):  
        try:
            msg = msg + f'\n cart value:: {maindata["cartValue"]} \n'
            # maindata["cartValue"]
            # maindata["productName"]
        except Exception as e:
            print(e)
            pass
        if purpose_id == 1:
            bot=telegram.Bot(token=data[0]["api_token"])
            chat_id=data[0]["chat_id"].split(',')
            print(chat_id)
            for i in range(0,len(chat_id)):
                print(1)
                bot.send_photo(chat_id=chat_id[i],photo=open(image_url, 'rb'),caption=msg)
                #2+2
        
        if purpose_id == 2:
            bot=telegram.Bot(token=data[1]["api_token"])
            chat_id=data[1]["chat_id"].split(',')
            print(chat_id)
            for i in range(0,len(chat_id)):
                bot.send_photo(chat_id=chat_id[i],photo=open(image_url, 'rb'),caption=msg)
                
                #2+2
                
    except Exception as e:
        print(e)
        pass


def alert_message(project_id,msg,ip_address):
    try:
        bot=telegram.Bot(token=data[0]["api_token"])
        chat_id=data[0]["chat_id"].split(',')
        print(chat_id)
        for i in range(0,len(chat_id)):
            bot_message=f'''
Error in Supertraffic
Project_id: {project_id}
error message: {msg}
machine ip address : {ip_address}
            '''
            bot.send_message(chat_id=chat_id[i],text=bot_message)
    except Exception as e:
        print(e)

#alert_message("133","test",requests.get('https://api.ipify.org').text)