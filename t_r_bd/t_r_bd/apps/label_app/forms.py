from django import forms

# BooleanField - флажок
# CharField - Текстовое поле ввода
# EmailField - Текстовое поле, Email
# PaswordField - текстовое поле, пароль
# ChoiceField - Выбор из нескольких вариантов
# DateField - Выбор даты
# DateTimeField -Даты и времени
# FileField - Загрузка файлов



class User_login(forms.Form):
	user_type = forms.ChoiceField(choices = ((1,"User"), (2,"Manager")))
	login = forms.CharField(max_length = 15)
	password = forms.CharField(max_length = 15)

	def clean_data(self):
		login = self.cleaned_data['login']
		password = self.cleaned_data['password']
		# if (Проверка на наличие в списках логинов и паролей введенных):
		# 	raise forms.ValidationError(
		# 		u'Данные выедены некорректно', code = 12)
		# return login,password

	def save(self):
		post = Post(**self.cleaned_data)
		post.save()
		return post
