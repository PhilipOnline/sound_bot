from django.shortcuts import render
from orders.models import Order

def ProfilePage(request):
    #print(request.user)

    #получаем объекты заказов отфильтрованных по текущему юзеру
    orders=Order.objects.all().filter(user=request.user)

    #for order in orders:
        #print(order.user,order.created)
    context = {'orders': orders}

    return render(request, 'profpage/profpage.html',context)

