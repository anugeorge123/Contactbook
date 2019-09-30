from django.shortcuts import render
from app3.models import Contactbook
from django.http import HttpResponse
import json

def contactbook1(request):
	return render(request,"first.html")
	
def crudops(request):
	dict1={}
	try:
		print("----Save----")
		na = request.POST['txt_name']
		print("name----->",na)
		no=request.POST['txt_no']
		print("no----->",no)
		
		if(na != "" and no !=""):
			if(no.isnumeric()==True):

				try:
					y = Contactbook.objects.get(name = na)
					print("y--->",y.name)
					if(y.name!=""):	
						print("Already Exist!")	
						dict1["val1"]="Already Exist!"
						dict1["status"]=True
					
				except Exception as e:
					#print("error-->",e)
					#print("already exist")
					contactbook=Contactbook(name=na,number=no)
					contactbook.save()
					print(contactbook)
					dict1["val2"]=na+" : "+no
					dict1["status"]=True
			else:
				dict1["val4"]="Please input numeric values only as contact number"
				dict1["status"]=False
		else:
			dict1["val3"]="Input field cannot be null"
			dict1['status']=False

		#dict1["val2"]=na+" : "+no
		#dict1["status"]=True

	except Exception as e:
		print(e)
		dict1["status"]=False
	print(dict1)
	jsondata=json.dumps(dict1)
	return HttpResponse(jsondata,content_type="application/json")

		
def view(request):
	dict2={}
	try:
		objects = Contactbook.objects.all()
		select ='---------------CONTACT BOOK-----------\n\n '
		for x in objects:
			select += x.name+" : "+x.number+" \n"
		print(select)
		
		dict2["val"]=select
		dict2["status"]=True
	except Exception as e:
		print(e)
		dict2["status"]=False
	print(dict2)
	jsondata=json.dumps(dict2)
	return HttpResponse(jsondata,content_type="application/json")


def update(request):
	return render(request,"updatecontact.html")
	

def updatefunction(request):
	dict3={}
	try:
		cname=request.POST['txt_cname']	
		print(cname)

		x = Contactbook.objects.get(name = cname)
		
		dict3["val1"]=x.name
		dict3["val2"]=x.number
		dict3["status"]=True
	except Exception as e:
		print("UpdateFunction->",e)
		dict3["status"]=False
	print(dict3)
	jsondata=json.dumps(dict3)
	return HttpResponse(jsondata,content_type="application/json")
	

def updatefunction1(request):
	dict4={}
	try:
		cname=request.POST['txt_cname']	
		print("cname --->",cname)
		newname=request.POST['txt_newname']
		print("-->",newname)
		newno=request.POST['txt_newno']
		print("--->",newno)

	
		contactbook = Contactbook.objects.get(name = cname)
		contactbook.name = newname
		contactbook.number = newno
		
		if(newname !="" and newno != ""):
			contactbook.save()
		else:
			dict4["vall"]="input field can not be null!"

		
		dict4["val1"]=newname
		dict4["val2"]=newno
		dict4["status"]=True
	except Exception as e:
		print("UpdateFunction1->",e)
		dict4["status"]=False
	print(dict4)
	jsondata=json.dumps(dict4)
	return HttpResponse(jsondata,content_type="application/json")

	


	
def delete(request):
	return render(request,"deletecontact.html")
	


def deletefunction(request):
	dict5={}
	try:
		cname=request.POST['txt_cname']	
		print(cname)

		x = Contactbook.objects.get(name = cname)
		
		dict5["val1"]=x.name
		dict5["val2"]=x.number
		dict5["status"]=True
	except Exception as e:
		print("UpdateFunction->",e)
		dict5["status"]=False
	print(dict5)
	jsondata=json.dumps(dict5)
	return HttpResponse(jsondata,content_type="application/json")


def deletefunction1(request):
	dict6={}
	try:
		cname=request.POST['txt_cname']	
		newname=request.POST['txt_newname']
		print(cname,"-->",newname)
		newno=request.POST['txt_newno']
		#res += '<br> Deleting an entry <br>'
		x = Contactbook.objects.get(name = newname)
		x.delete()
		#dict6["val1"]=newname
		#dict6["val2"]=newno
		dict6["status"]=True
	except Exception as e:
		print("DELETE Function->",e)
		dict6["status"]=False
	print(dict6)
	jsondata=json.dumps(dict6)
	return HttpResponse(jsondata,content_type="application/json")

