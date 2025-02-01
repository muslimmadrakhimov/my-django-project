from django.shortcuts import render

# Create your views here.
# Главная страница
def index(request):
    return render(request, 'third_task/index.html')

# Страница магазина
def shop(request):
    items = ["Игровая консоль", "Геймпад", "Игровой ПК"]
    return render(request, 'third_task/shop.html', {"items": items})

# Страница корзины
def cart(request):
    return render(request, 'third_task/cart.html')
