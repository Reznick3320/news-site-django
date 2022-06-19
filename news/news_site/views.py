
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm

# Create your views here.

class HomeNews(ListView):
    model = News
    template_name = 'news_site/index.html'
    context_object_name = 'news'
    paginate_by = 10
    # extra_context = {'title': 'Главная'}
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_pablished=True)

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news_site/index.html', context=context)




class NewsByCategory(ListView):
    model = News
    template_name = 'news_site/index.html'
    context_object_name = 'news'
    allow_empty = False #запрещает показ пустых списков
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk= self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_pablished=True)


# def get_categoty(request, category_id):
#     news = News.objects.filter(category_id = category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,

#     }
#     return render(request, 'news_site/category.html', context)





class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    # template_name = 'news_site/news_detail.html'
    context_object_name = 'news_item'

# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk = news_id)
#     return render(request, 'news_site/view_news.html', {'news_item': news_item})





class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news_site/add_news.html'
    # success_url = reverse_lazy('home') перенаправление после создания записи
    # login_url = '/admin/' если не авторизован, то перенаправит на авторизацию
    raise_exception = True


# def add_news(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             # new_news = News.objects.create(**form.cleaned_data)
#             new_news = form.save()
#             return redirect(new_news)
#     else:
#         form = NewsForm()
#     return render(request, 'news_site/add_news.html', {'form': form})

def register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'news_site/register.html', { 'form':form })

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news_site/login.html',{'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def contact_form(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'ruslan.reznick@ukr.net', ['reznick59@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = ContactForm()
    return render(request, 'news_site/contact_form.html', {'form': form})