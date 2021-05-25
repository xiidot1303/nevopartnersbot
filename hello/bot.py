
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
from hello.models import Account, Status, Profile, month, subscribersbot, typing, storage, security, changing
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(''))
load_dotenv(os.path.join(basedir, '.env'))
TOKEN = os.environ.get('TOKEN')


PORT = int(os.environ.get('PORT', 5000))


welcome = 'Добро пожаловать! \nВы можете просмотреть свои отчеты нажав на кнопку Отчеты или поменять настройки вашего аккаунта, нажав на кнопку Настройки'
start_text = 'Вы можете просмотреть свои отчеты нажав на кнопку Отчеты или поменять настройки вашего аккаунта, нажав на кнопку Настройки'


def start(update, context):
    bot = context.bot
    if subscribersbot.objects.filter(user_id=update.message.chat.id):
        if subscribersbot.objects.get(user_id = update.message.chat.id).parol=='r/e/q':
            t = typing.objects.get(user_id=update.message.chat.id)
            if t.parol == True:
                update.message.reply_text('Повторно введите пароль')
            else:
                i_back = InlineKeyboardButton(text='Назад', callback_data='start')
                i_yes = InlineKeyboardButton(text='Да', callback_data='deleteuser')
                mrk = InlineKeyboardMarkup([[i_back, i_yes]])
                update.message.reply_text('К этому профилю уже подключен другой пользователь.\nХотите авторизоваться и удалить другого пользователя?', reply_markup=mrk)
            
        elif subscribersbot.objects.get(user_id = update.message.chat.id).parol:
            login = subscribersbot.objects.get(user_id=update.message.chat.id).login
            if Profile.objects.get(login=login).tg_phone_number is None:
                i_contact = KeyboardButton(text='Отправить контакт', request_contact=True)
                mrk = ReplyKeyboardMarkup([[i_contact]], resize_keyboard=True)
                bot.send_message(update.message.chat.id, 'Для авторизации в системе вам необходимо отправить свой контакт. Пожалуйста, нажмите на кнопку «Отправить контакт».', reply_markup = mrk)
            else:
                i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
                i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
                mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])

                update.message.reply_text(start_text, reply_markup = mrk)
        else:
            update.message.reply_text('Повторно введите пароль')
            istyping = typing.objects.get(user_id=update.message.chat.id)
            istyping.parol = True
            istyping.save()
    else:
        update.message.reply_text('Введите логин')
        try:
            t = typing.objects.get(user_id=update.message.chat.id)
            t.login=True
            t.parol=False
            t.save()
        except:
            t = typing.objects.get_or_create(user_id=update.message.chat.id, login=True, parol=False)
        try:
            ch = changing.objects.get(user_id=update.message.chat.id)
            ch.login = False
            ch.parol = False
            ch.save()
        except:
            ch = changing.objects.get_or_create(user_id=update.message.chat.id, login=False, parol=False)
        
        

def callback_query(update, context):
    bot = context.bot
    c = update.callback_query
    if subscribersbot.objects.filter(user_id=c.message.chat.id):
        if c.data == 'home':
            login = subscribersbot.objects.get(user_id=c.message.chat.id).login
            if Profile.objects.filter(login=login)[0].tg_phone_number == None:
                i_contact = KeyboardButton(text='Отправить контакт', request_contact=True)
                mrk = ReplyKeyboardMarkup([[i_contact]], resize_keyboard=True)
                bot.send_message(c.message.chat.id, 'Для авторизации в системе вам необходимо отправить свой контакт. Пожалуйста, нажмите на кнопку «Отправить контакт».', reply_markup = mrk)
            else:
                
                i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
                i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
                mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])

                c.edit_message_text(start_text, reply_markup = mrk)
        if c.data == 'accounts':
            s = subscribersbot.objects.get(user_id = c.message.chat.id)
            obj = Profile.objects.get(login=s.login)
            all_accounts = Account.objects.filter(pseudonym=obj.pseudonym).order_by('year')
            
            if all_accounts:
                available = []
                items = []
                for i in all_accounts:
                    if i.year in available:
                        pass
                    else:
                        available.append(i.year)
                        items.append(InlineKeyboardButton(text=i.year, callback_data='year'+str(i.year)))
                i_back = InlineKeyboardButton(text = 'Назад', callback_data='home')
                
                buttons = []
                massiv = []
                for i in items:
                    massiv.append(i)
                    if len(massiv) == 3:
                        buttons.append(massiv)
                        massiv = []
                if massiv:
                    buttons.append(massiv)
                buttons.append([i_back])
                mrk = InlineKeyboardMarkup(buttons)
                
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Выберите год', reply_markup=mrk)
            else:
                i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
                i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
                mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
                bot.send_message(c.message.chat.id, 'Отчёты пока нет')
                bot.send_message(c.message.chat.id, start_text, reply_markup = mrk)
                
        
        if c.data[:4] == 'year':
            
            obj = storage.objects.get_or_create(user_id=c.message.chat.id)
            y = obj[0]
            
            y.year = int(c.data[4:])
            y.save()
            login = subscribersbot.objects.get(user_id = c.message.chat.id).login
            obj = Profile.objects.get(login=login)
            
            all_accounts = Account.objects.filter(pseudonym=obj.pseudonym, year = int(c.data[4:])).order_by('month_id')
            
            available = []
            items = []
            for i in all_accounts:
                if i.month in available:
                    pass
                else:
                    available.append(i.month)
                    status = i.status.s
                    try:
                        if status == 'Оплачен':
                            status = '✅'
                        elif status == 'В работе':
                            status = '☑️'
                        elif status == 'В ожидании':
                            status = '⏳'
                        elif status == 'Отклонена':
                            status = '❌'
                        elif status == 'Перенесена':
                            status = '➡️'
                    except:
                        status = ''
                    items.append(InlineKeyboardButton(text=status+i.month.month, callback_data='month'+str(i.month.month)))
            year = c.data[4:]
            buttons = []
            massiv = []
            for i in items:
                massiv.append(i)
                if len(massiv) == 3:
                    buttons.append(massiv)
                    massiv = []
            if massiv:
                buttons.append(massiv)
            i_back = InlineKeyboardButton(text = 'Назад', callback_data='accounts')
            buttons.append([i_back])
            markup = InlineKeyboardMarkup(buttons)
            
            c.edit_message_text('Год: '+year+'\nвыберите месяц', reply_markup=markup)
        
        if c.data[:5] == 'month':
            months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
            login = subscribersbot.objects.get(user_id = c.message.chat.id).login
            obj = Profile.objects.get(login=login)
        
            year = storage.objects.get(user_id=c.message.chat.id).year
            all_accounts = Account.objects.get(pseudonym = obj.pseudonym, year = year, month = months.index(c.data[5:]) + 1)
            i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
            i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
            mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
            if not all_accounts.card_number:
                kard = ''
            else:
                kard = '\n' + str(all_accounts.card_number)
    
    
            period = 'Период: '+ all_accounts.month.month + ' ' + str(all_accounts.year)
            endtext = ''
            if not all_accounts.status:
                status = "\nСтатус: Не оплачен"
            
            else:
                
                status = '\nСтатус: ' + all_accounts.status.s
            if not all_accounts.summa:
                summa = ''
            else:
                summa = '\nСумма: ' + str(all_accounts.summa)
            if all_accounts.day_payment[0] == '.':
                data_pay = ''
            else:
                data_pay = ' ' + all_accounts.day_payment
            text = period + summa + status + data_pay + kard + endtext
            c.edit_message_text(text)
            try:
                bot.send_document(c.message.chat.id, all_accounts.document)
            except:
                fwe = 0
            c.message.reply_text(start_text, reply_markup = mrk)
        
        if c.data == 'setting':
            i_da = InlineKeyboardButton(text = 'Обновить логин/пароль', callback_data='change_login')
            i_exit = InlineKeyboardButton(text = 'Выйти из аккаунта', callback_data='logout')
            i_back = InlineKeyboardButton(text = 'Назад', callback_data='home')
            mrk = InlineKeyboardMarkup([[i_da, i_exit], [i_back]])
            c.edit_message_text('Настройки\n\n Вы можете Сменить логин/пароль или\nВыйти из бота', reply_markup=mrk)
        if c.data == 'logout':
            i_da = InlineKeyboardButton(text = 'Да', callback_data='confirm_logout')
            i_back = InlineKeyboardButton(text = 'Назад', callback_data='setting')
            mrk = InlineKeyboardMarkup([[i_da, i_back]])
            c.edit_message_text('Вы действительно хотите выйти из бота?', reply_markup=mrk)
        if c.data == 'confirm_logout':
            c.edit_message_text('Вы вышли из своего профиля. Рекомендуем авторизоваться в боте, чтобы не пропустить новые уведомления и отчеты.\n\nнажмите /start, чтобы перезапустить бота')
            i = subscribersbot.objects.get(user_id=c.message.chat.id)
            changing.objects.get(user_id=i.user_id).delete()
            typing.objects.get(user_id=i.user_id).delete()
            
            try:
                storage.objects.get(user_id=i.user_id).delete()
            except:
                qpwomsqd = 0
            i.delete()
        if c.data == 'change_login':
            c.edit_message_text('Введите новый логин:')
            ch = changing.objects.get(user_id=c.message.chat.id)
            ch.login = True
            ch.save()
          
            
        if c.data == 'start':
            obj = subscribersbot.objects.get(user_id=c.message.chat.id)
            obj.delete()
            
            c.edit_message_text('Введите логин')
            try:
                t = typing.objects.get(user_id=c.message.chat.id)
                t.login = True
                t.parol = False
                t.save()
            except:
                t = typing.objects.get_or_create(user_id=c.message.chat.id, login=True, parol=False)
            try:
                ch = changing.objects.get(user_id=c.message.chat.id)
                ch.login = False
                ch.parol = False
                ch.save()
            except:
                ch = changing.objects.get_or_create(user_id=c.message.chat.id, login=False, parol=False)
            
            
    
        if c.data == 'deleteuser':
            
            i_back = InlineKeyboardButton(text='Назад', callback_data='start')
            mrk = InlineKeyboardMarkup([[i_back]])
            c.edit_message_text('Введите пароль', reply_markup=mrk)
            t = typing.objects.get(user_id=c.message.chat.id)
            t.parol = True
            t.save()
                
def contact(update, context):
    login = subscribersbot.objects.get(user_id=update.message.chat.id).login
    user = Profile.objects.get(login=login)
    user.tg_phone_number = str(update.message.contact.phone_number)
    user.save()
    
    update.message.reply_text('Успешная авторизация!', reply_markup=ReplyKeyboardRemove())

    
    i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
    i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
    mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
    update.message.reply_text(welcome, reply_markup = mrk)

def text(update, context):
    bot = context.bot
    try:
        ischanging = changing.objects.get(user_id = update.message.chat.id)
        istyping = typing.objects.get(user_id=update.message.chat.id)
    except:
        dwedewdw = 0
    if update.message.text == 'Главная':
        i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
        i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
        mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
        update.message.reply_text(start_text, reply_markup = mrk)
    elif istyping.login:
        if subscribersbot.objects.filter(login=update.message.text):
            i_back = InlineKeyboardButton(text='Назад', callback_data='start')
            i_yes = InlineKeyboardButton(text='Да', callback_data='deleteuser')
            mrk = InlineKeyboardMarkup([[i_back, i_yes]])
            update.message.reply_text('К этому профилю уже подключен другой пользователь.\nХотите авторизоваться и удалить другого пользователя?', reply_markup=mrk)
            subscribersbot.objects.create(user_id=update.message.chat.id, login='r/e/q' + update.message.text, parol = 'r/e/q')
            istyping.login = False
            istyping.save()
                       
        elif Profile.objects.filter(login=update.message.text):
            subscribersbot.objects.create(user_id=update.message.chat.id, login=update.message.text)
            istyping.login = False
            istyping.parol = True
            istyping.save()
            update.message.reply_text('Введите ваш пароль')
        else:
            update.message.reply_text('Неправильно, повторно введите логин')
    elif istyping.parol:
        current_login = subscribersbot.objects.get(user_id=update.message.chat.id)
        if current_login.parol == 'r/e/q':
            prof_obj = Profile.objects.get(login=current_login.login[5:])
            if prof_obj.parol == update.message.text:
                del_obj = subscribersbot.objects.get(login = prof_obj.login, parol = prof_obj.parol)
                login = subscribersbot.objects.get(user_id=update.message.chat.id).login
                current_login.login = login[5:]
                current_login.save()
                bot.send_message(del_obj.user_id, 'К Вашему профилю только что подключился другой пользователь. Если это были не вы то немедленно обратитесь Вашему менеджеру по работе с партнерами или по почты: support@nevo.uz')
                typing.objects.get(user_id = del_obj.user_id).delete()
                changing.objects.get(user_id = del_obj.user_id).delete()
                del_obj.delete()

                obj = subscribersbot.objects.get(user_id=update.message.chat.id)
                obj.parol = update.message.text
                obj.save()
                istyping.parol = False
                
                istyping.save()
                i_contact = KeyboardButton(text='Отправить контакт', request_contact=True)
                mrk = ReplyKeyboardMarkup([[i_contact]], resize_keyboard=True)
                try:
                    update.edit_message_text('Введите пароль')
                except:
                    dedede = 0
                bot.send_message(update.message.chat.id, 'Для авторизации в системе вам необходимо отправить свой контакт. Пожалуйста, нажмите на кнопку «Отправить контакт».', reply_markup = mrk)
            else:
                update.message.reply_text('Неправильно, введите пароль еще раз')

        
        elif Profile.objects.get(login=current_login.login).parol == update.message.text:
            obj = subscribersbot.objects.get(user_id=update.message.chat.id)
            obj.parol = update.message.text
            obj.save()
            istyping.parol = False
            istyping.save()
            i_contact = KeyboardButton(text='Отправить контакт', request_contact=True)
            mrk = ReplyKeyboardMarkup([[i_contact]], resize_keyboard=True)
            bot.send_message(update.message.chat.id, 'Для авторизации в системе вам необходимо отправить свой контакт. Пожалуйста, нажмите на кнопку «Отправить контакт».', reply_markup = mrk)
            
        else:
            update.message.reply_text('Неправильно, введите пароль еще раз')
    elif ischanging.login:
        subs = subscribersbot.objects.get(user_id = update.message.chat.id)
        prof = Profile.objects.get(login = subs.login)
        try:
            Profile.objects.get(login=update.message.text)
            update.message.reply_text('Этот логин доступен, пожалуйста, введите другой логин')
        except:
            subs.login = update.message.text
            prof.login = update.message.text
            subs.save()
            prof.save()
            ischanging.login = False
            ischanging.parol = True
            ischanging.save()
            update.message.reply_text('Логин, успешно изменен\n введите новый пароль:')
    elif ischanging.parol:
        subs = subscribersbot.objects.get(user_id = update.message.chat.id)
        prof = Profile.objects.get(login = subs.login)
        subs.parol = update.message.text
        prof.parol = update.message.text
        subs.save()
        prof.save()
        update.message.reply_text('Пароль успешно изменен')
        i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
        i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
        mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
        update.message.reply_text(start_text, reply_markup = mrk)
        ischanging.parol = False
        ischanging.save()


updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.contact, contact))
dp.add_handler(MessageHandler(Filters.text, text))
dp.add_handler(CallbackQueryHandler(callback_query))

