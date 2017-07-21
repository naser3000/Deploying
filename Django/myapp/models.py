from django.db import models
#from django.core.urlresolvers import reverse

from picklefield.fields import PickledObjectField
import re

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	avatar = models.FileField(default="")
	user_token = models.CharField(max_length=40)
	default_weblog = models.CharField(max_length=10)

	def __str__(self):
		return self.username



from celery import shared_task
class Weblog(models.Model):
	weblog_title = models.CharField(default="", max_length=250)
	weblog_auther = models.CharField(max_length=250)
	weblog_date = models.DateTimeField(max_length=50)
	user = models.ForeignKey(User, default=1)
	posts_words = models.CharField(default='', max_length=100000)
	word_dic = PickledObjectField(default={})

	def __str__(self):
		return self.weblog_auther



	@shared_task
	def add_words(weblog_id, txt):
		weblog = Weblog.objects.filter(id=weblog_id)
		dictionary = weblog[0].word_dic
		wordList = re.sub("[^\w]", " ",  txt).split()
		for w in wordList :
			if w in dictionary :
				dictionary[w] += 1
			else :
				dictionary[w] = 1
		weblog.update(word_dic=dictionary)





class Post(models.Model):
	post_title = models.CharField(max_length=50)
	post_summary = models.CharField(max_length=500)
	post_text = models.CharField(max_length=5000)
	post_date = models.DateTimeField(max_length=50)
	photo = models.FileField(default="")
	weblog = models.ForeignKey(Weblog, default=1)
	#user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.post_title


class Comment(models.Model):
	comment_auther = models.CharField(max_length=20)
	comment_text = models.CharField(max_length=500)
	comment_date = models.DateTimeField(max_length=50)
	post = models.ForeignKey(Post, default=1)

	def __str__(self):
		return self.comment_auther



