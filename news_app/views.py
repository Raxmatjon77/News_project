from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,ListView

from news_app.models import News, Category
from news_app.forms import  ContactForm
from  django.http import HttpResponse

def news_list(request):
    news_list=News.published.all()
    context={
        'news_list':news_list
    }
    return render(request,'news/news_list.html',context=context)
def news_detail(request,news):
    news=get_object_or_404(News,slug=news,status=News.Status.Published)
    context={
        "news":news
    }
    return render(request,"news/news_detail.html",context)
    
# def HomePageView(request):
#     categories=Category.objects.all()
#     local_one=News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
#     local_news=News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
#     news_list=News.published.all().order_by('-publish_time')[:10]
#     context={
#      'news_list':news_list,
#       'categories' :categories,
#         'local_news':local_news,
#        "local_one":local_one
#         }
    # return render(request,"news/index.html",context)
class HomePageView(ListView):
    model=News
    template_name='news/index.html'
    context_object_name='news'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        context['sport_xabarlari']=News.published.all().filter(category__name='sport').order_by('-publish_time')[0:6]
        context['xorij_xabarlari']=News.published.all().filter(category__name='xorijiy').order_by('-publish_time')[0:6]
        context['texnologiya_xabarlar']=News.published.all().filter(category__name='texnologiya').order_by('-publish_time')[0:6]
        context['mahalliy_xabarlar']=News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[0:6]

        context['news_list']=News.published.all().order_by('-publish_time')[:5]
        return context




def errorPageView(request):

    return render(request,'news/404.html')
def aboutPageView(request):

    return  render(request,'news/about.html')
#
class contactPageView(TemplateView):
    template_name = 'news/contact.html'
    def get(self,request,*args,**kwargs):
        form=ContactForm()
        context={
            'form':form
        }
        return render(request,'news/contact.html',context)
    def post(self,request,*args,**kwargs):
        form=ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2> biz bilan bog'langaningiz uchun tashakkur")
        context={
            'form':form
        }
        return render(request,'news/contact.html',context)
    

class LocalNewsView(ListView):
    model=News
    template_name='news/mahalliy.html' 
    context_object_name='mahalliy_yangiliklar' 
    def get_queryset(self):
        news=News.published.all().filter(category__name='Mahalliy')
        return news

class ForeignNewsView(ListView):
    model=News
    template_name='news/xorij.html' 
    context_object_name='xorij_yangiliklari' 
    def get_queryset(self):
        news=News.published.all().filter(category__name='xorijiy')
        return news

    

class TechnologyNewsView(ListView):
    model=News
    template_name='news/texnologiya.html' 
    context_object_name='texno_yangiliklar' 
    def get_queryset(self):
        news=News.published.all().filter(category__name='texnologiya')
        return news



class SportNewsView(ListView):
    model=News
    template_name='news/sport.html' 
    context_object_name='sport_yangiliklar'   
    def get_queryset(self):
        news=News.published.all().filter(category__name='sport')
        return news
 
