from django.shortcuts import render, HttpResponseRedirect
from .forms import studentregis
from .models import user
# Create your views here.
def addandshow(request):
    if request.method=='POST':
        fm=studentregis(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()
            fm=studentregis()
    else:
        fm=studentregis()
    stud=user.objects.all()
    return render(request, 'enrol/addandshow.html',{'form':fm,'stu':stud})


def delete_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        fm=studentregis(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=pi=user.objects.get(pk=id)
        fm=studentregis( instance=pi)
      
    return render(request,'enrol/update.html',{'form':fm})