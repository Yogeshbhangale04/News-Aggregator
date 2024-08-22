from django.urls import path
from news.views import scrape, news_list, about, overview, contactus, products
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('', news_list, name="home"),
  path('news/about', about, name='about'),
  path('news/overview', overview, name='overview'),
  path('news/contactus', contactus, name='contactus'),
  path('news/products', products, name='products')
  
]