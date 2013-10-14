#-*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Article, Categorie

class ArticleAdmin(admin.ModelAdmin):
	list_display	= ('titre', 'auteur', 'date', 'apercu_contenu')
	list_filter	= ('auteur', 'categorie',)
	date_hierarchy	= 'date'
	ordering	= ('date', )
	search_fields	= ('titre', 'contenu')
	fields		= ('titre', 'slug', 'auteur', 'categorie', 'contenu')

	def apercu_contenu(self, article):
		"""retourne les 40 premiers caractères d'un article s'il y en a plus complète avec des points de suspension """
		text = article.contenu[0:40]
		if len(article.contenu) > 40:
			return '%s...' % text
		else:
			return text
		
	apercu_contenu.short_description = u"apercu du contenu"
			
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
