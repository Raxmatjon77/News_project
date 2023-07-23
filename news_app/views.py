from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
# from django.core.paginator import _SupportsPagination
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,CreateView,View
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from news_app.models import News, Category,Comment
from news_app.forms import  ContactForm,CommentForm
from  django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from news_project.custom_permissions import OnlyLoggedSuperUser
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import News, Comment, Contact



def news_list(request):
    news_list=News.published.all()
    context={
        'news_list':news_list
    }
    return render(request,'news/news_list.html',context=context)
def news_detail(request,news):
    news=get_object_or_404(News,slug=news,status=News.Status.Published)
    context = {}
    #hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits
    comments=news.comments.filter(active=True)
    comment_count=comments.count()
    new_comment=None
    if request.method == "POST":
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
         # commentni DB ga saqlamaymiz

            new_comment=comment_form.save(commit=False)
            #izox egasini so'rov yuborayotgan userga bog'ladik
            new_comment.news=news
            new_comment.user=request.user
            # commentni DB ga saqlaymiz
            new_comment.save()
            comment_count=comment_count+1
            comment_form=CommentForm()
    else:
        comment_form=CommentForm()
    context={
        "news":news,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'comment_count':comment_count

    }
    return render(request,"news/news_detail.html",context)



class HomePageView(ListView):
    model=News
    template_name='news/index.html'
    context_object_name='news'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        context['sport_xabarlari']=News.published.all().filter(category__id=7).order_by('-publish_time')[0:5]
        context['xorij_xabarlari']=News.published.all().filter(category__id=6).order_by('-publish_time')[0:5]
        context['texnologiya_xabarlar']=News.published.all().filter(category__id=8).order_by('-publish_time')[0:5]
        context['mahalliy_xabarlar']=News.published.all().filter(category__id=5).order_by('-publish_time')[0:5]
        context['popular_posts']=News.published.all()[5:10]
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
        popular_posts=News.published.all()[5:10]
        form=ContactForm()
        context={
            'popular_posts':popular_posts,
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
        news=News.published.all().filter(category__id=5)
        return news

class ForeignNewsView(ListView):
    model=News
    template_name='news/xorij.html' 
    context_object_name='xorij_yangiliklari' 
    def get_queryset(self):
        news=News.published.all().filter(category__id=6)
        return news

    

class TechnologyNewsView(ListView):
    model=News
    template_name='news/texnologiya.html' 
    context_object_name='texno_yangiliklar' 
    def get_queryset(self):
        news=News.published.all().filter(category__id=8)
        return news



class SportNewsView(ListView):
    model=News
    template_name='news/sport.html' 
    context_object_name='sport_yangiliklar'   
    def get_queryset(self):
        news=News.published.all().filter(category__id=7)
        return news
class NewsUpdateView(OnlyLoggedSuperUser,UpdateView):
    model=News
    fields=('title','image','body','status','category')
    template_name='crud/news_edit.html'

    def form_valid(self,form):
        self.News = form.save(commit=False)
        if not self.News.slug:
            self.News.slug = slugify(self.News.title)
        self.News.save()
        return super().form_valid(form)
class NewsDeleteView(OnlyLoggedSuperUser,DeleteView):
    model=News
    template_name='crud/news_delete.html'
    success_url=reverse_lazy('home_page')
class NewsCreateView(OnlyLoggedSuperUser,CreateView):
    model=News
    fields=('title','slug','image','body','status','category',)
    template_name='crud/news_create.html'
    def form_valid(self,form):
        self.News=form.save(commit=False)
        if not self.News.slug:
            self.News.slug=slugify(self.News.title)
        self.News.save()
        return super().form_valid(form)
@login_required
@user_passes_test(lambda u:u.is_superuser)

def admin_page_view(request):
    admin_users=User.objects.filter(is_superuser=True)
    context={
        'admin_users':admin_users
    }
    return render(request,"pages/admin_page.html",context)
class SearchresultList(ListView):
    model=News
    template_name='news/search_result.html'
    context_object_name='news_list'
    def get_queryset(self):
        query=self.request.GET.get('q')
        return News.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    #
from django.db.models import Count

def get_popular_posts(request):
  """
  Returns a list of the most popular posts, based on the number of hunts.
  """
  posts = News.objects.all()
  return posts[6:10]


def index(request):
  popular_posts = get_popular_posts(request)
  context = {
    'popular_posts': popular_posts,
  }
  return render(request, 'news/index.html', context)
