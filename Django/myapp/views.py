from django.template.defaultfilters import date as change_format
from django.views.decorators.csrf import csrf_exempt
from .models import Weblog, Post, Comment, User
from django.template import loader
from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime
import json


def index(request):
	return HttpResponse("<h1>Hello world! it's  my first live website</h1>")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////     R E G I S T E R      //////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from .forms import Register
@csrf_exempt
def register(request):
	res = {"status": 0}
	if request.method=='POST':
	#************************** making request ******************************
		key = request.POST.keys()
		value = request.POST.values()
		#*************************** validation ******************* start ********
		if len(value) < 5:
			res["status"] = -1
			res["message"] = "invalid student number"
			return HttpResponse(json.dumps(res), content_type="application/json")
		dic ={key[0] : value[0],
			key[1] : value[1],
			key[2] : value[2],
			key[3] : value[3],
			key[4] : value[4],
		}
	#************************** making response *******************************
		'''form = Register(request.POST)
		print('+++++++++++++++++++++++++')
		print(form)
		print(form.errors)
		if form.is_valid():
			print('@@@@@@@@@@@@@@@@@@@@@')
			return HttpResponse(json.dumps(form), content_type="application/json")
		else :
			print('!!!!!!!!!!!!!!!!!!!!!!')
			print(form.errors)
			return HttpResponse(json.dumps(form.errors), content_type="application/json")'''

		user_q=User.objects.filter(username=dic['student_number'])
		if len(user_q.values())>0:
		#if dic['student_number']=='hahahihi':
			res["status"] = -1
			res["message"] = "user already exists"
			return HttpResponse(json.dumps(res), content_type="application/json")
		if dic['student_number']=='':
			res["status"] = -1
			res["message"] = "invalid student number"
			return HttpResponse(json.dumps(res), content_type="application/json")
		elif len(dic['password']) <= 7:
			res["status"] = -1
			res["message"] = "too short password"
			return HttpResponse(json.dumps(res), content_type="application/json")
		elif dic['first_name']=='':
			res["status"] = -1
			res["message"] = "first name needed"
			return HttpResponse(json.dumps(res), content_type="application/json")
		elif dic['last_name']=='':
			res["status"] = -1
			res["message"] = "last name needed"
			return HttpResponse(json.dumps(res), content_type="application/json")
		elif dic['email']=='':
			res["status"] = -1
			res["message"] = "email needed"
			return HttpResponse(json.dumps(res), content_type="application/json")
		#*************************** validation ********************* end ********
		new_user = User()
		new_user.username = dic['student_number']
		new_user.password = dic['password']
		new_user.first_name = dic['first_name']
		new_user.last_name = dic['last_name']
		new_user.email = dic['email']
		new_user.save()

		#CELERY
		#send_feedback_email_task.delay()





		new_weblog = Weblog()
		new_weblog.weblog_auther = new_user.username
		new_weblog.weblog_date = datetime.now()
		new_weblog.user = new_user
		new_weblog.save()
	#*********************** end making request *******************************
	else:
		res["status"] = -1
		res["message"] = 'invalid student number'
	
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////     L O G I N      ///////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@csrf_exempt
def login(request):
	res = {"status": 0}
	if request.method=='POST':
	#************************** making request ******************************
		key = request.POST.keys()
		value = request.POST.values()
		#*************************** validation ******************* start ********
		if len(value) < 2:
			res["status"] = -1
			res["message"] = "user not found"
			return HttpResponse(json.dumps(res), content_type="application/json")
		dic ={key[0] : value[0],
			key[1] : value[1],
		}
		username = dic['student_number']
		password = dic['password']
		if username == '':
			res["status"] = -1
			res["message"] = "user not found"
			return HttpResponse(json.dumps(res), content_type="application/json")
		if password == '':
			res["status"] = -1
			res["message"] = "wrong password"
			return HttpResponse(json.dumps(res), content_type="application/json")
		user_q = User.objects.filter(username=username)
		if len(user_q.values())==0:
			res["status"] = -1
			res["message"] = "user not found"
			return HttpResponse(json.dumps(res), content_type="application/json")
		elif user_q.values()[0]['password']!=password:
			res["status"] = -1
			res["message"] = "wrong password"
			return HttpResponse(json.dumps(res), content_type="application/json")

		#*************************** validation ********************* end ********
	#*********************** end making request *******************************
	#**************************************************************************
	#************************** making response *******************************
		#print('********************')
		res["token"] = token_generation()
		#print('+++++++++++++++++++++++++++++')
		user_q.update(user_token = res["token"])
		#print('############################')
	else:
		res["status"] = -1
		res["message"] = 'user not found'
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////    D E F A U L T    W E B L O G    ///////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@csrf_exempt
def default_weblog(request):
	res = {"status": 0}
	#************************** token validation **********************************
	if 'HTTP_X_TOKEN' in request.META:
		token = request.META.__getitem__('HTTP_X_TOKEN')
		user_q = User.objects.filter(user_token=token)
		if len(user_q) == 0 :
			res["status"] = -1
			res["message"] = 'no/wrong token'
			return HttpResponse(json.dumps(res), content_type="application/json")
	else :
		#print('==='*100)
		res["status"] = -1
		res["message"] = 'no/wrong token'
		return HttpResponse(json.dumps(res), content_type="application/json")
	#************************** end token validation *******************************
	#************************** making request ********************************
	#weblog_id = request.POST.keys(.....)
	#key = request.POST.keys()
	#1value = request.POST.values()
	#*********************** end making request *******************************
	if request.method=='POST':
		res["status"] = -1
		res["message"] = 'user not found'
	#**************************************************************************
	#************************** making response *******************************
	else:
		if user_q[0].default_weblog == '':
			weblog_q = Weblog.objects.filter(user=user_q).aggregate(Min('id'))
			user_q.update(default_weblog = weblog_q['id__min'])
			res["weblog_id"] = weblog_q['id__min']
		else :
			res["weblog_id"] = user_q[0].default_weblog 
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////     S H O W I N G    P O S T S    ///////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@csrf_exempt
def show_posts(request):
	res = {"status": 0}
	if request.method=='GET':
		key = request.GET.keys()
		value = request.GET.values()
		dic ={key[0] : value[0],
		}
		q = Post.objects.filter(id = dic['id'])
		if len(q) == 0 :
			res["status"] = -1
			res["message"] = 'not found'
			return HttpResponse(json.dumps(res), content_type="application/json")
		res = {"status": 0, "post":[]}
		for b in q:
			res["post"].append({
				"title" : b.post_title ,
				"summary" : b.post_summary ,
				"text" : b.post_text ,
				"datetime" : change_format(b.post_date, "D M d H:i:s Y") ,
			})
	#************************** making response *******************************
	else:
		key = request.POST.keys()
		value = request.POST.values()
		#*************************** validation ******************* start ********
		if len(value) < 1:
			res["status"] = -1
			res["message"] = "can't be empty"
			return HttpResponse(json.dumps(res), content_type="application/json")
		if (value[0]==''):
			res["status"] = -1
			res["message"] = "can't be empty"
			return HttpResponse(json.dumps(res), content_type="application/json")
		#*************************** validation ********************* end ********
		dic ={key[0] : value[0],
		}
		weblog_q = Weblog.objects.filter(id=dic['weblog_id'])
		if len(weblog_q) == 0 :
			res["status"] = -1
			res["message"] = "not found"
			return HttpResponse(json.dumps(res), content_type="application/json")
		post_q = Post.objects.filter(weblog__id=dic['weblog_id'])
		#res["weblog_id"] = weblog_q['id__min']
		res["posts"] = []
		for p in post_q:
			res["posts"].append({
				"id" : p.id ,
				"title" : p.post_title ,
				"summary" : p.post_summary ,
				"datetime" : change_format(p.post_date, "D M d H:i:s Y") ,
			})
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////    C R E A T I N G   P O S T    ////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=Post)
def save_profile(sender, instance, **kwargs):
	total_txt = instance.post_title +' '+ instance.post_summary +' '+ instance.post_text
	instance.weblog.add_words.delay(instance.weblog.id, total_txt)



@csrf_exempt
def create_post(request):
	res = {"status": 0}
	#************************** token validation **********************************
	#print('//'*50)
	#print(request.META)
	#print('//'*50)
	if 'HTTP_X_TOKEN' in request.META:
		#print('!!!'*50)
		#print(request.META.__getitem__('HTTP_X_TOKEN'))
		token = request.META.__getitem__('HTTP_X_TOKEN')
		user_q = User.objects.filter(user_token=token)
		if len(user_q) == 0 :
			res["status"] = -1
			res["message"] = 'no/wrong token'
			return HttpResponse(json.dumps(res), content_type="application/json")
	else :
		#print('==='*100)
		res["status"] = -1
		res["message"] = 'no/wrong token'
		return HttpResponse(json.dumps(res), content_type="application/json")
	#************************** end token validation *******************************
	if request.method=='POST':
	#************************** making request **********************************
		new_obj = Post()
		key = request.POST.keys()
		value = request.POST.values()
		#weblog_id = request.url(....)
		#*************************** validation ******************* start ********
		if len(value) < 4:
			res["status"] = -1
			res["message"] = "can't be empty"
			return HttpResponse(json.dumps(res), content_type="application/json")
		if (value[0]=='' or value[1]=='' or value[2]==''):
			res["status"] = -1
			res["message"] = "can't be empty"
			return HttpResponse(json.dumps(res), content_type="application/json")
		#*************************** validation ********************* end ********
		dic ={key[0] : value[0],
			key[1] : value[1],
			key[2] : value[2],
			key[3] : value[3],
		}
		#print(dic)
		new_obj.post_title = dic['title']
		new_obj.post_summary = dic['summary']
		new_obj.post_text = dic['text']
		new_obj.post_date = datetime.now()
		weblog_q = Weblog.objects.filter(id=dic['weblog_id']).filter(user=user_q[0])
		if (len(weblog_q) == 0):
			res["status"] = -1
			res["message"] = "u can't"
			return HttpResponse(json.dumps(res), content_type="application/json")

		#print('&&&&&&&&&&&&&&&&')
		#print(weblog_q[0].id)
		new_obj.weblog = weblog_q[0]
		#total_txt = new_obj.post_title +' '+ new_obj.post_summary +' '+ new_obj.post_text
		#new_obj.weblog.add_words.delay(weblog_q[0].id, total_txt)
		new_obj.save()
		# task here to post
		#AddWeblogWords(new_obj)
	#*********************** end making request *******************************
	#**************************************************************************
	#************************** making response *******************************
		res["post_id"] = new_obj.id
	else:
		res["status"] = -1
		res["message"] = 'not found'
	
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////    S H O W I N G    C O M M E N T S    /////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@csrf_exempt
def show_comments(request):
	res = {"status": 0}
	#************************** token validation **********************************
	'''
	print('//'*50)
	#print(request.META)
	print('//'*50)
	if 'HTTP_X_TOKEN' in request.META:
		print('!!!'*50)
		print(request.META.__getitem__('HTTP_X_TOKEN'))
		token = request.META.__getitem__('HTTP_X_TOKEN')
		user_q = User.objects.filter(user_token=token)
		if len(user_q) == 0 :
			res["status"] = -1
			res["message"] = 'no/wrong token'
			return HttpResponse(json.dumps(res), content_type="application/json")
	else :
		print('==='*100)
		res["status"] = -1
		res["message"] = 'no/wrong token'
		return HttpResponse(json.dumps(res), content_type="application/json")
	'''
	#************************** end token validation *******************************
	if request.method=='POST':
	#************************** making request ******************************
		res["status"] = -1
		res["message"] = 'not found'
		return HttpResponse(json.dumps(res), content_type="application/json")
	#*********************** end making request *******************************
	#**************************************************************************
	#************************** making response *******************************
	else:
		key = request.GET.keys()
		value = request.GET.values()
		dic ={key[0] : value[0],
		}
		#print(user_q[0])
		#q = Post.objects.filter(id = dic['post_id']).filter(user=user_q[0])
		q = Post.objects.filter(id = dic['post_id'])
		if len(q) == 0 :
			res["status"] = -1
			res["message"] = 'not found'
			return HttpResponse(json.dumps(res), content_type="application/json")
		res = {"status": 0, "comments":[]}
		q = Comment.objects.filter(post_id = dic['post_id'])
		for b in q:
			res["comments"].append({
				"datetime" : change_format(b.comment_date, "D M d H:i:s Y") ,
				"text" : b.comment_text ,
			})
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////    C R E A T I N G   C O M M E N T    /////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@csrf_exempt
def create_comment(request):
	res = {"status": 0}
	#************************** token validation **********************************
	'''
	if 'HTTP_X_TOKEN' in request.META:
		token = request.META.__getitem__('HTTP_X_TOKEN')
		user_q = User.objects.filter(user_token=token)
		if len(user_q) == 0 :
			res["status"] = -1
			res["message"] = 'no/wrong token'
			return HttpResponse(json.dumps(res), content_type="application/json")
	else :
		res["status"] = -1
		res["message"] = 'no/wrong token'
		return HttpResponse(json.dumps(res), content_type="application/json")
	'''
	#************************** end token validation *******************************
	if request.method=='POST':
	#************************** making request ******************************
		key = request.POST.keys()
		value = request.POST.values()
		#*************************** validation ******************* start ********
		if len(value) < 2:
			res["status"] = -1
			res["message"] = "can't be empty"
			return HttpResponse(json.dumps(res), content_type="application/json")
		if (value[0]=='' or value[1]==''):
			res["status"] = -1
			res["message"] = "can't be empty"
			return HttpResponse(json.dumps(res), content_type="application/json")
		#*************************** validation ********************* end ********
		dic ={key[0] : value[0],
			key[1] : value[1],
		}
		post_q = Post.objects.filter(id = dic['post_id'])
		if len(post_q) == 0 :
			res["status"] = -1
			res["message"] = 'not found'
			return HttpResponse(json.dumps(res), content_type="application/json")
		new_obj = Comment()
		#new_obj.comment_auther = user_q[0].username
		new_obj.comment_auther = 'Unknown'
		new_obj.comment_text = dic['text']
		new_obj.comment_date = datetime.now()
		new_obj.post = post_q[0]
		#print(new_obj.post)
		#print(post_q[0])
		new_obj.save()
	#*********************** end making request *******************************
	#**************************************************************************
	#************************** making response *******************************
		res['comment'] = { 'datetime' : change_format(new_obj.comment_date, "D M d H:i:s Y"),
		'text': dic['text'],
		}
	else:
		res["status"] = -1
		res["message"] = "can't be empty"
	
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////    D E F A U L T    W E B L O G 'S    P O S T S    //////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@csrf_exempt
def default_weblog_posts(request):
	res = {"status": 0}
	#************************** token validation **********************************
	if 'HTTP_X_TOKEN' in request.META:
		token = request.META.__getitem__('HTTP_X_TOKEN')
		user_q = User.objects.filter(user_token=token)
		if len(user_q) == 0 :
			res["status"] = -1
			res["message"] = 'no/wrong token'
			return HttpResponse(json.dumps(res), content_type="application/json")
	else :
		#print('==='*100)
		res["status"] = -1
		res["message"] = 'no/wrong token'
		return HttpResponse(json.dumps(res), content_type="application/json")
	#************************** end token validation *******************************
	#************************** making request ********************************
	#weblog_id = request.POST.keys(.....)
	#key = request.POST.keys()
	#1value = request.POST.values()
	#*********************** end making request *******************************
	if request.method=='POST':
		res["status"] = -1
		res["message"] = 'user not found'
	#**************************************************************************
	#************************** making response *******************************
	else:
		weblog_q = Weblog.objects.filter(user=user_q).aggregate(Min('id'))
		post_q = Post.objects.filter(weblog__id=weblog_q['id__min'])
		#res["weblog_id"] = weblog_q['id__min']
		res["posts"] = []
		for p in post_q:
			res["posts"].append({
				"id" : p.id ,
				"title" : p.post_title ,
				"summary" : p.post_summary ,
				"datetime" : change_format(p.post_date, "D M d H:i:s Y") ,
			})
		res["weblog_id"] = weblog_q['id__min']
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////    T O K E N   G E N E R A T I O N    ///////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from django.utils.crypto import get_random_string
import random
def token_generation():
	a = get_random_string(length=40)
	return a



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////  S E A R C H I N G  //////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import operator
import re
def search(request):
	
	if request.method == 'POST' :
		txt = request.POST['q']
		wordList = re.sub("[^\w]", " ",  txt).split()
		if len(wordList) < 2 or len(wordList) > 10 :
			return render(request, 'weblog/search.html', {"error_message": "invalid input: please enter 2-10 words"})
		'''for word in wordList :
			weblog_q = Weblog.objects.filter(word_dic__contains = word)
			print(weblog_q)'''

		search_result = {}
		#context = {'weblogs' : []}
		weblog_q = Weblog.objects.all()
		#print('@@@@@@@@@@@@@@@@@@@@@@@@')
		#print (wordList)
		for weblog in weblog_q :
			for word in wordList :
				#print (weblog.word_dic)
				if word in weblog.word_dic :
					#print('*************************')
					#print (weblog)
					#print(weblog.word_dic)
					if weblog in search_result :
						search_result[weblog] += weblog.word_dic[word]
					else :
						search_result[weblog] = weblog.word_dic[word]

	else :
		search_result = {}
		#template_name = 'weblog/search.html'
	#context['weblogs'] = search_result
	sort_result = sorted(search_result.items(), key=operator.itemgetter(1))
	context = {'weblogs': reversed(sort_result)}
	#print('+++++++++++++++++++++')
	#print(search_result)
	'''print (context['weblogs'])
	print(sort_result)'''
	return render(request, 'weblog/search.html', context)

	'''
	x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
	context['weblogs'] = search_result.keys()
	context = {'weblogs': sorted(search_result.items())}
	print(sorted(search_result.iteritems()))
	print (context)
	return render(request, 'weblog/search.html', context)'''
	




#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def showw(request):
	return HttpResponse("<h1>Success, OK!</h1>")


def show(request):
	p#rint(request.method)
	if request.method=='GET':
		a = ''
		#print('*'*20)
		#print(request.POST)
		#print('*'*20)
	else:
		return redirect('/')





def tsting(request):
	res = {"status": 0}
	
	#**************************************************************************user not found
	#************************** making response *******************************
	res = {"status": 0, "posts":[]}
	q = Post.objects.all()
	for b in q:
		res["posts"].append({
			"id" : b.id ,
			"title" : b.post_title ,
			"summary" : b.post_summary ,
			"datetime" : b.post_date ,
		})
	#*********************** end making response *******************************
	if request.method=='POST':
	#************************** making request ******************************
		key = request.POST.keys()
		value = request.POST.values()
		dic ={key[0] : value[0],
			key[1] : value[1],
		}
		username = dic['student_number']
		password = dic['password']
		#*********************** end making request *******************************
		#print('*'*50)
		#print(request.POST.keys())
		#print(request.POST.values())
		#print('*'*50)
		return HttpResponse(json.dumps(res), content_type="application/json")
		#return HttpResponse(qq)
		#return HttpResponse("<h1>login POST</h1>")
	else:
		res["status"] = -1
		res["message"] = 'user not found'
	#*********************** end making response *******************************
	return HttpResponse(json.dumps(res), content_type="application/json")