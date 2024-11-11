from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def main_page(request):
    if request.method == 'GET':
        return HttpResponse("""
                            <h1>Это главное меню:</h1>
                            <a href='about_me/'>about_me</a><br/>
                            <a href = 'about_cars/'>about_cars</a><br/>
                            <a href = 'system_time/'>system_time</a><br/>
                            """)

def about_me_response(request):
    if request.method == 'GET':
        return HttpResponse("""
                            <h1>About me</h1>
                            <h2>name : Islam</h2>
                            <h2>age : 20</h2>
                            <h2>group : 46-1 backend</h2>
                            """)
    
def about_my_cars_response(request):
    if request.method == 'GET':
        return HttpResponse("""
                            <p>У меня нет питомцев так что сделаю с машинами хоть машин у меня и нет XD</p>
                            <p>Гемера</p>
                            <img src = 'https://d62-a.sdn.cz/d_62/c_img_E_F/vAjGV/koenigsegg-gemera-rychlost.jpeg?fl=cro,0,51,1713,964%7Cres,1200,,1%7Cjpg,80,,1' >
                            """)

def system_time(request):
    if request.method == 'GET':
        return HttpResponse(f"""
                            <h1>{datetime.now()}</h1>
                            """)