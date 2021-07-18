from django.db import models

class Account(models.Model):
    pseudonym = models.CharField(null=True, max_length=40, verbose_name="Псевдоним")
    
    month = models.ForeignKey('month', null=True, on_delete=models.PROTECT, verbose_name="Месяц")
    year=models.IntegerField(null=True, verbose_name="Год")
    status = models.ForeignKey('Status', null = True, on_delete=models.PROTECT, verbose_name="Статус", blank=True)
    day_payment = models.CharField(verbose_name="Дата оплата", blank=True, null=True, max_length=30)
    document = models.FileField(upload_to='%Y/%m/%d/', null=True, blank=True)
    summa = models.CharField(max_length=20, null=True, blank=True, verbose_name="")
    published = models.DateTimeField(db_index = True, null=True, auto_now_add=True, blank=True)
    card_number = models.CharField(max_length=50, null=True, verbose_name="", blank=True)
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарии')

    notification = models.CharField(max_length=20, verbose_name='Уведомления', blank=True)
class Status(models.Model):
    s = models.CharField(max_length=20, db_index=True, null=True)
    def __str__(self):
        return self.s

class Profile(models.Model):
    published = models.CharField(max_length=50, null=True, verbose_name='Дата заключение договора')
    login = models.CharField(null=True, max_length=50, verbose_name="Логин")
    parol = models.CharField(null=True, max_length=50, verbose_name="Парол")
    pseudonym = models.CharField(null=True, max_length=50, verbose_name="Псевдоним")
    number = models.CharField(max_length=20, blank=True, verbose_name="")
    code = models.CharField(max_length=17, blank=True, verbose_name="", null=True)
    name = models.CharField(max_length=50, blank=True, verbose_name="ФИО")
    prefix = models.CharField(max_length=20, null=True, verbose_name='ID партнера')
    type_payment = models.CharField(max_length=50, null=True, verbose_name='Способ оплаты', blank=True)
    valute_card = models.CharField(max_length=10, null=True, verbose_name='Валюта карты', blank=True)
    card_number = models.CharField(max_length=30, null=True, verbose_name='', blank=True)
    date_card = models.CharField(max_length=20, null=True, blank=True, verbose_name='Срок карты')
    owner_card = models.CharField(null=True, max_length=100, verbose_name='Владелец карты', blank=True)

    date_birthday = models.CharField(max_length=30, null=True, blank=True, verbose_name='Дата рождения')
    number_passport = models.CharField(max_length=20, null=True, blank=True, verbose_name='Серия и номер паспорта')
    date_passport = models.CharField(max_length=30, null=True, blank=True, verbose_name='Дата выдачи паспорта')
    who_gave = models.CharField(max_length=100, null=True, blank=True, verbose_name='Кем выдан')
    place_registration = models.CharField(max_length=100, null=True, blank=True, verbose_name='Место регистрации')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='E-mail')
    bank = models.CharField(max_length=100, null=True, blank=True, verbose_name='Банк')
    reward = models.CharField(max_length=200, blank=True, null=True, verbose_name='Вознаграждение')
    passport_main_st = models.FileField(verbose_name='Паспорт главная ст.', blank=True)
    passport_st_registration = models.FileField(verbose_name='Паспорт ст. регистрации', blank=True)
    signed_contract = models.FileField(verbose_name='Подписанный договор', blank=True)
    inn = models.CharField(verbose_name="ИНН", blank=True, null=True, max_length=200)

    tg_phone_number = models.CharField(null=True, max_length=40, blank=True)

    comment = models.TextField(blank=True, null=True, verbose_name='Комментарии')
    type_document = models.CharField(blank=True, null=True, max_length=50)
    photo = models.FileField(upload_to='profile_photos/', null=True, blank=True)


    
class month(models.Model):
    month = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.month
        
class card(models.Model):
    pseudonym = models.CharField(max_length=50, null=True)
    card_number = models.CharField(max_length=50, null=True)
    type_payment = models.CharField(max_length=50, null=True, blank=True)
    valute_card = models.CharField(max_length=10, null=True, blank=True)
    card_number = models.CharField(max_length=30, null=True, blank=True)
    owner_card = models.CharField(null=True, max_length=100, blank=True)

class subscribersbot(models.Model):
    user_id = models.IntegerField(null=True)
    login = models.CharField(null=True, max_length=100)
    parol = models.CharField(null=True, max_length=100, blank=True)
    
class typing(models.Model):
    user_id = models.IntegerField(null=True)
    login = models.BooleanField(primary_key=False, blank=True)
    parol = models.BooleanField(primary_key=False, blank=True)
class changing(models.Model):
    user_id = models.IntegerField(null=True)
    login = models.BooleanField(primary_key=False, blank=True)
    parol = models.BooleanField(primary_key=False, blank=True)
class storage(models.Model):
    user_id = models.IntegerField(null=True)
    year = models.IntegerField(null=True, blank=True)

class security(models.Model):
    parol = models.CharField(null=True, max_length=100)



class stories(models.Model):   #all stories otchets and profiles, for table
    published = models.DateTimeField(db_index = True, null=True, auto_now_add=True)
    admin = models.CharField(max_length=100, null=True)
    obj = models.CharField(max_length=20, null=True)
    text = models.TextField(null=True)
    obj_id = models.IntegerField(null=True, blank=True)


class acc_pre_value(models.Model):
    pseudonym = models.CharField(null=True, max_length=40, verbose_name="Псевдоним")
    
    month = models.CharField(null=True, max_length=100)
    year=models.IntegerField(null=True, verbose_name="Год")
    status = models.CharField(null=True, max_length=100)
    day_payment = models.CharField(verbose_name="Дата оплата", null=True, max_length=40)
    document = models.FileField(upload_to='%Y/%m/%d/', null=True)
    summa = models.CharField(max_length=20, null=True)
    card_number = models.CharField(max_length=50, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарии')

    notification = models.CharField(max_length=20, verbose_name='Уведомления', null=True)
class prof_pre_value(models.Model):
    published = models.CharField(max_length=50, null=True, verbose_name='Дата заключение договора')
    login = models.CharField(null=True, max_length=50, verbose_name="Логин")
    parol = models.CharField(null=True, max_length=50, verbose_name="Парол")
    pseudonym = models.CharField(null=True, max_length=50, verbose_name="Псевдоним")
    number = models.CharField(blank=True, verbose_name="", null=True, max_length=100)
    code = models.CharField(max_length=5, blank=True, verbose_name="t", null=True)
    name = models.CharField(max_length=50, blank=True, verbose_name="name")
    prefix = models.CharField(max_length=20, null=True)
    type_payment = models.CharField(max_length=50, null=True, blank=True)
    valute_card = models.CharField(max_length=10, null=True, blank=True)
    card_number = models.CharField(max_length=30, null=True, blank=True)
    date_card = models.CharField(max_length=20, null=True, blank=True)
    owner_card = models.CharField(null=True, max_length=100, blank=True)

    
    date_birthday = models.CharField(max_length=30, null=True, blank=True, verbose_name='Дата рождения')
    number_passport = models.CharField(max_length=20, null=True, blank=True, verbose_name='Серия и номер паспорта')
    date_passport = models.CharField(max_length=30, null=True, blank=True, verbose_name='Дата выдачи паспорта')
    who_gave = models.CharField(max_length=100, null=True, blank=True, verbose_name='Кем выдан')
    place_registration = models.CharField(max_length=100, null=True, blank=True, verbose_name='Место регистрации')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='E-mail')
    bank = models.CharField(max_length=100, null=True, blank=True, verbose_name='Банк')
    reward = models.CharField(max_length=200, blank=True, null=True, verbose_name='Вознаграждение')
    passport_main_st = models.FileField(verbose_name='Паспорт главная ст.', blank=True)
    passport_st_registration = models.FileField(verbose_name='Паспорт ст. регистрации', blank=True)
    signed_contract = models.FileField(verbose_name='Подписанный договор', blank=True)


    inn = models.CharField(verbose_name="ИНН", blank=True, null=True, max_length=200)

    tg_phone_number = models.CharField(null=True, max_length=40, blank=True)

    comment = models.TextField(blank=True, null=True, verbose_name='Комментарии')
    type_document = models.CharField(blank=True, null=True, max_length=50)
    photo = models.FileField(upload_to='profile_photos/', null=True, blank=True)



class sendmessage(models.Model):
    published = models.DateTimeField(db_index = True, null=True, auto_now_add=True)
    admin = models.CharField(max_length=50, null=True)
    select = models.CharField(max_length=50, null=True)
    message = models.TextField(max_length=500, null=True)
    user = models.CharField(max_length=50, null=True)



class happybirthday(models.Model):
    message = models.TextField(verbose_name='Текст для отправки', null=True)
    hour = models.CharField(max_length=10, null=True, verbose_name='')
    minute = models.CharField(max_length=10, null=True, verbose_name=':')    #verbose_name=':'

class contract(models.Model):
    file = models.FileField(upload_to='contract/main', null=True)


class Audio(models.Model):
    composition = models.CharField(null=True, max_length=200, verbose_name='Произведение', blank=True)
    artist = models.CharField(null=True, max_length=100, verbose_name='Артист', blank=True)
    autor_music = models.CharField(null=True, max_length=100, verbose_name='Автор музыки', blank=True)
    autor_text = models.CharField(null=True, max_length=100, verbose_name='Автор текста', blank=True)
    album = models.CharField(null=True, max_length=100, verbose_name='Альбом', blank=True)
    isrc = models.CharField(null=True, max_length=100, verbose_name='ISRC (код)', blank=True)
    genre = models.CharField(null=True, max_length=50, verbose_name='Жанр', blank=True)
    copyright = models.CharField(null=True, max_length=100, verbose_name='Авторские права', blank=True)
    related_rights = models.CharField(null=True, max_length=100, verbose_name='Смежные права', blank=True)
    upc = models.CharField(null=True, max_length=100, verbose_name='UPC', blank=True)
    release_date = models.CharField(null=True, max_length=100, verbose_name='Дата релиза', blank=True)
    territory = models.CharField(null=True, max_length=100, verbose_name='Территория', blank=True)
    link = models.CharField(null=True, max_length=200, verbose_name='Ссылка на файл', blank=True)
    pseudonym = models.CharField(null=True, blank=True, max_length=100)
    status = models.CharField(null=True, blank=True, max_length=5)
    is_generate = models.BooleanField(blank=True, default=False)
    number_of_file = models.CharField(null=True, blank=True, max_length=20)


class Video(models.Model):
    composition = models.CharField(null=True, max_length=200, verbose_name='Произведение', blank=True)
    type = models.CharField(null=True, max_length=100, verbose_name='Тип', blank=True)
    artist = models.CharField(null=True, max_length=100, verbose_name='Артист', blank=True)
    isrc = models.CharField(null=True, max_length=100, verbose_name='ISRC (код)', blank=True)
    producer = models.CharField(null=True, max_length=100, verbose_name='Режиссер-постановщик', blank=True)
    operator = models.CharField(null=True, max_length=100, verbose_name='Оператор-постановщик', blank=True)
    autor_script = models.CharField(null=True, max_length=100, verbose_name='Автор сценария', blank=True)
    painter = models.CharField(null=True, max_length=100, verbose_name='Художник-постановщик', blank=True)
    copyright = models.CharField(null=True, max_length=100, verbose_name='Авторские права', blank=True)        
    release_date = models.CharField(null=True, max_length=100, verbose_name='Дата релиза', blank=True)
    territory = models.CharField(null=True, max_length=100, verbose_name='Территория', blank=True)
    link = models.CharField(null=True, max_length=200, verbose_name='Ссылка на файл', blank=True)
    pseudonym = models.CharField(null=True, blank=True, max_length=100)
    status = models.CharField(null=True, blank=True, max_length=5)
    is_generate = models.BooleanField(blank=True, default=False)
    number_of_file = models.CharField(null=True, blank=True, max_length=20)