from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Client, Trainer, SubscriptionPlan, Visit
from .forms import ClientForm

def index(request):
    """Главная страница со статистикой"""
    stats = {
        'clients_count': Client.objects.count(),
        'trainers_count': Trainer.objects.count(),
        'subscriptions_count': SubscriptionPlan.objects.count(),
        'visits_count': Visit.objects.count(),
    }
    return render(request, 'index.html', {'stats': stats})

def client_list(request):
    """Список клиентов с пагинацией"""
    clients = Client.objects.select_related('subscription', 'trainer').all()
    paginator = Paginator(clients, 10)  # 10 клиентов на страницу
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'clients/list.html', {'page_obj': page_obj})

def client_detail(request, pk):
    """Детальная страница клиента"""
    client = get_object_or_404(Client, pk=pk)
    visits = Visit.objects.filter(client=client).order_by('-visited_at')[:10]
    return render(request, 'clients/detail.html', {
        'client': client, 
        'visits': visits
    })

def client_create(request):
    """Добавление нового клиента"""
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/form.html', {
        'form': form, 
        'title': 'Добавить клиента'
    })

def trainer_list(request):
    """Список тренеров"""
    trainers = Trainer.objects.all()
    return render(request, 'trainers/list.html', {'trainers': trainers})

def subscription_list(request):
    """Список абонементов"""
    subscriptions = SubscriptionPlan.objects.all()
    return render(request, 'subscriptions/list.html', {'subscriptions': subscriptions})
