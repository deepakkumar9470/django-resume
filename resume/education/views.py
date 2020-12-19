from django.shortcuts import render

# Create your views here.
def skill_set(request):
    context = {'myskill':'active'}
    return render(request,'edu/skills.html',context)