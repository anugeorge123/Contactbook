from django.urls import path
from . import views

urlpatterns = [
    path('',views.contactbook1,name='first'),
	
	path('contactbook/',views.crudops,name='First Page of The HTML'),
	path('contactbook1/',views.view,name='View of the Contact Book'),
	path('contactbook2/',views.update,name='update'),
	path('contactbook2/contactbook3/',views.updatefunction,name='search using name'),
	path('contactbook2/contactbook4/',views.updatefunction1,name='update name and number'),
	path('contactbook5/',views.delete,name='delete contact'),
	path('contactbook5/contactbook6/',views.deletefunction,name='search using name'),	
	path('contactbook5/contactbook7/',views.deletefunction1,name='delete contact'),
]
