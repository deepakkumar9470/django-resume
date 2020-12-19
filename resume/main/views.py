from django.shortcuts import render

# Create your views here.
def home_show(request):
    context = {'myhome':'active'}
    return render(request,'main/home.html',context)

def contact_show(request):
    context = {'mycontact':'active'}
    return render(request,'main/contact.html',context)