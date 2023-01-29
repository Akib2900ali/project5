from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from  .forms import UserForm

def aboutUs(request):
    return render (request,'index.html')

def userform(request):
    finalans=0
    fn=UserForm()
    data={'form':fn}
    try:
     if request.method=="post":  
      n1=int(request.post['num1'])
      n2=int(request.post['num2'])
      print(n1+n2);
      finalans=n1+n2
      data={
           'n1':n1,
           'n2':n2,
           'output':finalans
      }
      
      return HttpResponseRedirect('/aboutUs/')

    except:
         pass  
    return render(request,'userform.html',{'output':finalans})    

def submitform(request):
     return HttpResponse(request)



