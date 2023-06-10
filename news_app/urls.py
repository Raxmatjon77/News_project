from django.urls import path
from .views import news_list, news_detail,HomePageView,contactPageView,errorPageView,aboutPageView,\
LocalNewsView,ForeignNewsView,SportNewsView,TechnologyNewsView,NewsUpdateView,NewsDeleteView

urlpatterns=[
    path("",HomePageView.as_view(),name="home_page"),
    path('news/',news_list,name='all_news_list'),
    path("news/<slug:news>/",news_detail,name='news_detail_page'),
    path('news/<slug>/edit/',NewsUpdateView.as_view(),name='update_page'),
    path('news/<slug>/delete/',NewsDeleteView.as_view(),name='delete_page'),
    path( 'contact-us/',contactPageView.as_view(),name='contact_page'),
    path( '404_page/',errorPageView,name='404_page'),
    path('about-us',aboutPageView,name='about_page'),
    path('local-news/',LocalNewsView.as_view(),name='local_news_page'),
    path('sport_news/',SportNewsView.as_view(),name='sport_news_page'),
    path('technology-news/',TechnologyNewsView.as_view(),name='technology_news_page'),
    path('foreign-news/',ForeignNewsView.as_view(),name='foreign_news_page'),

]