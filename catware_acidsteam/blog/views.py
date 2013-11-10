#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from blog.forms import ContactForm, ArticleForm
from datetime import datetime

def home(request):
	"""Affiche les articles du blog"""
	articles = Article.objects.all() 	
	return render(request, 'blog/home.html', {'derniers_articles':articles})

def read(request, id, slug):
	"""Affiche un article complet"""
	article = get_object_or_404(Article, id=id, slug=slug)
	return render(request, 'blog/read.html', {'article':article})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		
		if form.is_valid():
			
			sujet = form.cleaned_data['sujet']
			message = form.cleaned_data['message']
			envoyeur = form.cleaned_data['envoyeur']
			renvoi = form.cleaned_data['renvoi']

			envoi = True
		
	else:
		form = ContactForm()

	return render(request, 'blog/contact.html', locals())	

def article(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = ArticleForm(instance=article)
	
	return render(request, 'blog/article.html', locals())							
def list_articles(request, month, year):
	text = "Vous avez demandé les articles de {0} {1}".format(month, year)
	return HttpResponse(text)		

def tpl(request):
	return render(request, 'blog/tpl.html', {'current_date': datetime.now()})
	
def addition(request, number1, number2):
	total = int(number1) + int(number2)
	return render(request, 'blog/addition.html', locals())		
