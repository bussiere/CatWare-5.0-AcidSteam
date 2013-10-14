#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from datetime import datetime

def home(request):
	"""Affiche les articles du blog"""
	articles = Article.objects.all() 	
	return render(request, 'blog/home.html', {'derniers_articles':articles})

def read(request, id, slug):
	"""Affiche un article complet"""
	article = get_object_or_404(Article, id=id, slug=slug)
	return render(request, 'blog/read.html', {'article':article})

def list_articles(request, month, year):
	text = "Vous avez demandé les articles de {0} {1}".format(month, year)
	return HttpResponse(text)		

def tpl(request):
	return render(request, 'blog/tpl.html', {'current_date': datetime.now()})
	
def addition(request, number1, number2):
	total = int(number1) + int(number2)
	return render(request, 'blog/addition.html', locals())		
