from django.shortcuts import render

def aboutUs(request):
    return render (request,'index.html')

def userform(request):
    finalans=0
    try:
        
      n1=int(request.GET['num1'])
      n2=int(request.GET['num2'])
      print(n1+n2);
      finalans=n1+n2
    except:
         pass  
    return render(request,'userform.html',{'output':finalans})    





