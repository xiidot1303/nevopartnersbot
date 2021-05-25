from datetime import datetime
import time
from hello.models import happybirthday, Profile, subscribersbot
import telegram
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(''))
load_dotenv(os.path.join(basedir, '.env'))
TOKEN = os.environ.get('TOKEN')

def update():
    my_token = TOKEN
    bot = telegram.Bot(token=my_token)
    
    
    obj = happybirthday.objects.get(pk=1)
    date = datetime.now()
    if str(date.hour) == str(obj.hour) and str(date.minute) == str(obj.minute):
        for p in Profile.objects.all():
            year, month, day = p.date_birthday.split('-')
            try:
                if int(date.month) == int(month) and int(date.day) == int(day):
                    
                    user_id = subscribersbot.objects.get(login=p.login).user_id
                    msg = obj.message
                    if "{partner}" in msg:
                        msg = msg.replace("{partner}", p.name)
                    bot.sendMessage(chat_id=user_id, text=msg)
            except:
                dededede = 9
                    
            
            
