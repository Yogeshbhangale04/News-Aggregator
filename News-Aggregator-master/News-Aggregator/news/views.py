from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

# Create your views here.
#

# from django.shortcuts import render, redirect

# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# https://github.com/sakship31/News-Aggregator?tab=readme-ov-file
def scrape(request, name):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}

    # get url as we change name/path
    url = f"https://www.theonion.com/{name}"

    # get content of news
    content = session.get(url).content

    soup = BSoup(content, "html.parser")

    News = soup.find_all("div", {"class": "sc-cw4lnv-13 hHSpAQ"})

    for article in News:
        main = article.find_all("a", href=True)

        linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
        link = linkx["href"]


# get title of news
        titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
        title = titlex.text

# get image of news
        imgx = article.find("img")["data-src"]

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = imgx
        new_headline.save()
    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        "object_list": headlines,
    }
    return render(request, "news/home.html", context)
def about(request):
    return render(request, "news/about.html")

def contactus(request):
    return  render(request, 'news/contactus.html')

def products(request):
    return render(request, 'news/productus.html')

def overview(request):
    return render(request,"news/overview.html")