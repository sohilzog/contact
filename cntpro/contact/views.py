from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact
from .forms import ContactRegisterForm
from django.contrib.auth import authenticate,login,logout



# Create your views here.
class ContactView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class ContactRegister(View):
    def get(self, request):
        form=ContactRegisterForm()
        return render(request,'contact.html',{'form':form})
    def post(self,request):
        fname=request.POST.get("name")
        email=request.POST.get("email")
        phno=request.POST.get("phnno")
        Contact.objects.create(name=fname,email=email,phnno=phno)
        messages.success(request,'contact created successfully')
        return render(request,'index.html')
    
class ContactList(View):
    def get(self, request):
        contacts=Contact.objects.all()
        return render(request,'list_contact.html',{'contacts':contacts})


class DeleteContact(View):
    def get(self, request,*args,**kwargs):
        id=kwargs.get('id')
        contact=Contact.objects.get(id=id)
        contact.delete()
        messages.error(request,'contact deleted successfully')

        return redirect('list_view')


class UpdateContact(View):
    def get(self, request,*args,**kwargs):
        id=kwargs.get('id')
        contact=Contact.objects.get(id=id)
        form=ContactRegisterForm(instance=contact)
        
        return render(request,'update_contact.html',{'contact':contact,'form':form})
    def post(self,request,*args,**kwargs):
        fname=request.POST.get("name")
        email=request.POST.get("email")
        phno=request.POST.get("phnno")
        contact=Contact.objects.get(id=kwargs.get("id"))
        contact.name=fname
        contact.email=email
        contact.phnno=phno
        contact.save()
        messages.success(request,'contact updated successfully')
        return redirect('list_view')

        
    

