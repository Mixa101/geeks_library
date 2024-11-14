from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

def main_page(request):
    if request.method == 'GET':
        return HttpResponse("<h1> THIS IS MAIN PAGE </h1>")

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


def book_list(request):
    books = models.Books.objects.all()
    if request.method == 'GET':
        return render(request, 'book.html', context = {'books':books})

def book_detail(request, book_id):
    books_detail = get_object_or_404(models.Books, id=book_id)
    if request.method == 'GET':
        return render(request, 'book_detail.html', context={'book': books_detail})
