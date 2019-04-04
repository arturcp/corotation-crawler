from django.shortcuts import render
from django.http import HttpResponse
from .models import Spider

def crawlerView(request):
    spider = Spider()
    return render(request, "crawler.html", { 'clusters': spider.clusters })