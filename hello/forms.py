from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date
from django.contrib.auth.models import User

class DateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5,'5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')]

        years = [(year, year) for year in [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
        years.insert(0, ('....', '...'))
        widgets = [
            
            forms.Select(attrs={'class': 'form-control',}, choices=months),
            forms.Select(attrs={'class': 'form-control',}, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '.':
                year, month = ['...', '...']    
            else:
                
                month, year = value.split('/')


            return [month, year]
        return [None, None]

    def value_from_datadict(self, data, files, name):

        #month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        month = data['date_card_0']
        year = data['date_card_1']
        return '{}/{}'.format(month, year)


class OldDateSelector(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5,'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')]

        years = [(year, year) for year in range(2000, 2031)]
        years.insert(0, ('....', '...'))
        widgets = [
            forms.Select(attrs={'class': 'form-control',}, choices=days),
            forms.Select(attrs={'class': 'form-control',}, choices=months),
            forms.Select(attrs={'class': 'form-control',}, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '-':
                year, month, day = ['...', '...', '...']    
            else:
                year, month, day = value.split('-')

            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)    




class NewDateSelector(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5,'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')]

        years = [(year, year) for year in range(2000, 2031)]
        years.insert(0, ('....', '...'))
        widgets = [
            forms.Select(attrs={'class': 'form-control',}, choices=days),
            forms.Select(attrs={'class': 'form-control',}, choices=months),
            forms.Select(attrs={'class': 'form-control',}, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '-':
                day, month, year = ['...', '...', '...']    
            else:
                day, month, year = value.split('-')

            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(day, month, year)    




class DateBirthday(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5,'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')]

        years = [(year, year) for year in range(1920, 2022)]
        years.insert(0, ('....', '...'))
        widgets = [
            forms.Select(attrs={'class': 'form-control',}, choices=days),
            forms.Select(attrs={'class': 'form-control',}, choices=months),
            forms.Select(attrs={'class': 'form-control',}, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '-':
                year, month, day = ['...', '...', '...']    
            else:
                year, month, day = value.split('-')

            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)    


class AccForm(ModelForm):
    
    class Meta:
        model = Account
        
        fields = {'pseudonym', 'month', 'year', 'status', 'day_payment', 'document', 'summa', 'card_number', 'comment', 'notification'}
        required = {
            'card_number': False,
            'summa': False,
        }
        widgets = {
            'notification': forms.Select(choices=[('Вкл', 'Вкл'), ('Выкл', 'Выкл')]),
            'day_payment': OldDateSelector,
            'pseudonym': forms.TextInput(attrs={'class': 'form-control'}),
            'month': forms.Select(choices=[(0, '--------'), (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=[(1, "Оплачен"), (2, "В ожидании"), (3, "В работе"), (4, "Отклонена")], attrs={'class': 'form-control'}),
            'summa': forms.TextInput(attrs={'class': 'form-control'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            

            
            
            }
    field_order = ['pseudonym', 'day_payment', 'month', 'summa', 'card_number', 'year', 'status', 'document', 'notification', 'comment']


class ProfForm(ModelForm):

    class Meta:
        model = Profile
        fields = {'login', 'parol', 'pseudonym','number', 'name', 'prefix', 
        'type_payment', 'valute_card', 'card_number', 'date_card', 'owner_card', 'published', 'date_birthday', 
        'number_passport', 'date_passport', 'who_gave', 'place_registration', 'email', 'bank', 'reward', 'passport_main_st', 'passport_st_registration', 'signed_contract', 'inn', 'comment'}
        labels = {
            'parol': 'Пароль'
        }
        widgets = {
            "date_birthday": DateBirthday,
            "date_passport": DateBirthday,
            "date_card": DateSelectorWidget,
            "published": OldDateSelector,
            "valute_card": forms.Select(choices=[('USD', 'USD'), ('RUB', 'RUB')], attrs={'class': 'form-control'}),
            
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'parol': forms.TextInput(attrs={'class': 'form-control',}),
            'pseudonym': forms.TextInput(attrs={'class': 'form-control',}),
            'code': forms.TextInput(attrs={'class': 'form-control',}),
            'number': forms.TextInput(attrs={'class': 'form-control',}),
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'prefix': forms.TextInput(attrs={'class': 'form-control',}),
            'type_payment': forms.TextInput(attrs={'class': 'form-control',}),
            'card_number': forms.TextInput(attrs={'class': 'form-control',}),
            'owner_card': forms.TextInput(attrs={'class': 'form-control',}),
            "published": OldDateSelector,
            
            'number_passport': forms.TextInput(attrs={'class': 'form-control',}),
            'who_gave': forms.TextInput(attrs={'class': 'form-control',}),
            'place_registration': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.TextInput(attrs={'class': 'form-control',}),
            'bank': forms.TextInput(attrs={'class': 'form-control',}),
            'reward': forms.TextInput(attrs={'class': 'form-control',}),
            'inn': forms.TextInput(attrs={'class': 'form-control',}),
            
            
        }
    field_order = ['login','type_payment', 'parol', 'valute_card', 'prefix', 'card_number', 'date_card', 'pseudonym', 'owner_card', 'name', 'bank', 'date_birthday', 'reward', 'number_passport', 
    'published', 'date_passport', 'passport_main_st', 'passport_st_registration', 'who_gave', 'signed_contract', 'place_registration', 'number', 'email', 'inn', 'comment']
class SecurityForm(ModelForm):
    class Meta:
        model = security
        fields = {'parol'}
        widgets = {
            "parol": forms.PasswordInput(),
            
            

        }



class SendmessageForm(forms.Form):
    select = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

    field_order = ['select', 'message']





class Addadmin(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=30, required=False)
    email = forms.CharField(max_length=100, required=True)
    title = forms.CharField(required=True, widget=forms.Select(choices=[('Бухгалтерия', 'Бухгалтерия'), ('Менеджер', 'Менеджер'), ('Аналитик', 'Аналитик')]), label='Роль админа')




class HappybirthdayForm(ModelForm):
    class Meta:
        model = happybirthday
        fields = {'message', 'hour', 'minute'}
        hours = [('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09')]
        for i in range(10, 24):
            hours.append((str(i), str(i)))
        minutes = [('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09')]
        for i in range(10, 61):
            minutes.append((str(i), str(i)))
        widgets = {
            'hour': forms.Select(choices=hours),
            'minute': forms.Select(choices=minutes)
        }

    field_order = ['message', 'hour', 'minute']


class ContractForm(ModelForm):
    class Meta:
        model = contract
        fields = {'file'}
    field_order = ['file']



class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = {'composition', 'type', 'artist', 'isrc', 'producer', 'operator', 'autor_script', 'painter', 'copyright', 'release_date', 'territory', 'link'}

        widgets = {
            'composition': forms.TextInput(attrs={'class': 'form-control'}), 
            'type': forms.TextInput(attrs={'class': 'form-control'}), 
            'artist': forms.TextInput(attrs={'class': 'form-control'}), 
            'isrc': forms.TextInput(attrs={'class': 'form-control'}), 
            'producer': forms.TextInput(attrs={'class': 'form-control'}), 
            'operator': forms.TextInput(attrs={'class': 'form-control'}), 
            'autor_script': forms.TextInput(attrs={'class': 'form-control'}), 
            'painter': forms.TextInput(attrs={'class': 'form-control'}), 
            'copyright': forms.TextInput(attrs={'class': 'form-control'}), 
            'release_date': NewDateSelector,
            'territory': forms.TextInput(attrs={'class': 'form-control'}), 
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }

    field_order = ['composition', 'type', 'artist', 'isrc', 'producer', 'operator', 'autor_script', 'painter', 'copyright', 'release_date', 'territory', 'link']

class AudioForm(ModelForm):
    class Meta:
        model = Audio
        fields = {'composition', 'artist', 'autor_music', 'autor_text', 'album', 'isrc', 'genre', 'copyright', 'related_rights', 'upc', 'release_date', 'territory', 'link'}
       
        widgets = {
            'composition': forms.TextInput(attrs={'class': 'form-control'}), 
            'artist': forms.TextInput(attrs={'class': 'form-control'}), 
            'autor_music': forms.TextInput(attrs={'class': 'form-control'}), 
            'autor_text': forms.TextInput(attrs={'class': 'form-control'}), 
            'album': forms.TextInput(attrs={'class': 'form-control'}), 
            'isrc': forms.TextInput(attrs={'class': 'form-control'}), 
            'genre': forms.TextInput(attrs={'class': 'form-control'}), 
            'copyright': forms.TextInput(attrs={'class': 'form-control'}), 
            'related_rights': forms.TextInput(attrs={'class': 'form-control'}), 
            'upc': forms.TextInput(attrs={'class': 'form-control'}), 
            'release_date': NewDateSelector,
            'territory': forms.TextInput(attrs={'class': 'form-control'}), 
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }

    field_order = ['composition', 'artist', 'autor_music', 'autor_text', 'album', 'isrc', 'genre', 'copyright', 'related_rights', 'upc', 'release_date', 'territory', 'link']


