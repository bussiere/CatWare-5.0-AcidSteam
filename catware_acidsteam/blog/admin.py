from django.contrib import admin
from blog.models import Article, Categorie

class ArticleAdmin(admin.ModelAdmin):
	list_display	= ('titre', 'auteur', 'date')
	list_filter	= ('auteur', 'categorie',)
	date_hierarchy	= 'date'
	ordering	= ('date', )
	search_fields	= ('titre', 'contenu')

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
