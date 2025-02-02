from django.shortcuts import render

# Create your views here.
# Главная страница
def index(request):
    return render(request, 'fourth_task/index.html')

# Магазин (обновляем context)
def shop(request):
    context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2" ]}
    return render(request, 'fourth_task/shop.html', context)

# Корзина
def cart(request):
    return render(request, 'fourth_task/cart.html')