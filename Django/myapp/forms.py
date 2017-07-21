from django import forms

class Register(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)
	email = forms.CharField(max_length=20)
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)

	def clean_username(self):
		username = self.cleaned_data.get('student_number')
		#print('!!!!!$$$$$$$$$$$$$$$$$!!!!!!!!!')
		#print(username)
		if username == "" :
			raise forms.ValidationError("invalid student number")
		user_q=User.objects.filter(username=username)
		if len(user_q.values())>0:
			raise forms.ValidationError("user already exists")
		return username