#-*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def home(request):
	text = """<center><h1>CatWare-4.0.0.1-AcidSteaM #dev</h1></br>
		<p>P4R4D0X1 Prod</p></center>"""
	return HttpResponse(text)

def list_articles(request, month, year):
	text = "Vous avez demandé les articles de {0} {1}".format(month, year)
	return HttpResponse(text)		

def tpl(request):
	return render(request, 'blog/tpl.html', {'current_date': datetime.now()})
	
def addition(request, number1, number2):
	total = int(number1) + int(number2)
	return render(request, 'blog/addition.html', locals())		
