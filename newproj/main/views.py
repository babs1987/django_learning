from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
#представление на основе функций

tips =(
'1. Если вы не управляете новостями, которые доходят до вас, значит, они управляют вами.',
'2. Работайте только с теми людьми, с кем вы хотели бы после работы выпить чай/кофе.',
'3. Не держите гаджеты в спальне.',
'4. Засыпайте «сегодня», а просыпайтесь «завтра».',
'5. Не держите почтовую программу постоянно открытой.',

)



def index(request, tip_index:int):
    # return HttpResponse("Главная страница приложения main проекта helloworld")
    return render(
        request,
        'main/base.html',
        {
            'head_title': 'Главная',
            'body_title': 'Добро пожаловать',
            #'align': '',
            'text': tips[tip_index],

        }
    )
