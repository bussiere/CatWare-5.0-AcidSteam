#-*- coding: utf-8 -*-
from django import forms
from models import Article

class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	envoyeur = forms.EmailField(label=u"Votre adresse mail")
	renvoi = forms.BooleanField(help_text=u"Cochez si vous souhaitez recevoir une copie du mail", required=False)

	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		sujet = cleaned_data.get('sujet')
		message = cleaned_data.get('message')

		if sujet and message:
			if "lama" in sujet and "lama" in message:
				msg = u"Il y a des lamas dans le sujet et le message on n'a pas assez de place pour accueillir autant de lama allez voir sur bordeau"
				self._errors["message"] = self.error_class([msg])
				
				del cleaned_data["message"]

		return cleaned_data

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
