from django.urls import path, include
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
from hello.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('security/', open_site),
    path('folder/', folder, name='folder'),
    path('', folder),
    path('profiles/', Profiles, name='profiles'), 
    path('add/account', AccCreateView.as_view(), name='createacc'),
    path('add/profile', ProfCreateView.as_view(), name = 'createprof'),
    path('delete/<int:pk>/', ProfDeleteView.as_view(), name='delprof'),
    path('afterdeleting/<str:ps>/<str:login>/', afterdeleting),
    path('account/<str:pse>/', accounts, name='account'),
    path('update/<int:pk>', AccEditView.as_view(), name='edit'),
    path('new/<int:pk>', ProfDetailView.as_view()),
    path('detail/<int:pk>', AccDetailView.as_view()),
    path('accupdate/<int:pk>', AccUpdateView.as_view()),
    path('editpassword/<int:pk>/', SecEditView.as_view()),
    path('admin/', admin.site.urls),
    path('bot/start/', StartBotView.as_view()),
    path('editprofile/<int:pk>', ProfEditView.as_view(), name='editprofile'),
    path('sendmessage/<str:ps>/<str:issent>', Sendmessage, name='sendmessage'),
    path('allaccounts/', allaccounts, name='allaccount'),
    path('accounts/login/', LoginView.as_view()),
    path('changepassword/', PasswordChangeView.as_view(template_name = 'registration/change_password.html'), name='editpassword'),
    path('changepassword/done/', PasswordChangeDoneView.as_view(template_name = 'bot/newpassword.html'), name='password_change_done'),
    path('deleteacc/<int:pk>/', AccDeleteView.as_view(), name='deleteacc'),
    path('profilessortby/<str:ps>/<str:by>/', SortProfiles, name='sortprof'),
    path('allaccountssort/<str:ps>/<str:status>/<str:year>/<str:month>/', sortallaccounts, name='sortacc'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sortfolder/<str:ps>/', sortfolder, name='sortfolder'),
    path('addadmin/', addadmin, name='addadmin'),
    path('files/<str:y>/<str:m>/<str:d>/<str:f>/', sendfile),
    path('admins/', admins, name = 'admins'),
    path('deladmin/<int:pk>', deladmin, name='deladmin'),
    path('files/<str:f>', senddocument),
    path("robots.txt", robots_txt),
    path('1459466926:AAFc46DpUlV1d7NiMxLhtY4abHhaGpQsu5I', bot_webhook, name='bot'),
    path('updatehbd/<int:pk>/', HappybirthdayEditView.as_view(), name='updatehbd'),

    path('calendar/', calendar, name='calendar'),
    path('files/contract/<str:ps>/', Contract, name='contract'),
    path('uploadcontract/<int:pk>/', ContractEditView.as_view(), name='edit_contract'),
    path('files/contract/main/<str:file>/', get_contract_main),


    
    path('content/<str:ps>', content, name='content'),
    
    path('add/audio/<str:artist>/<int:extra>/', audio_create, name='create_audio'),
    path('add/video/<str:artist>/<int:extra>/', video_create, name='create_video'),
    
    path('audio_detail/<int:pk>', AudioDetailView.as_view()),
    path('video_detail/<int:pk>', VideoDetailView.as_view()),
    
    path('delete_audio/<int:pk>', delete_audio, name='delaudio'),
    path('delete_video/<int:pk>', delete_video, name='delvideo'),

    path('update_audio/<int:pk>', AuidoEditView.as_view(), name='edit_audio'),
    path('update_video/<int:pk>', VideoEditView.as_view(), name='edit_video'),
    
    path('add_app_file/<str:artist>', generation_file, name='add_app_file'),
    path('app_list/<str:artist>', app_list, name='app_list'),
    path('open_app_file/<str:app>', open_app, name='open_app'),
]   


