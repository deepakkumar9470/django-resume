from django.shortcuts import render

# Create your views here.
def services(request):
      context = {'myservices':'active'}
      return render(request,'serv/services.html',context)