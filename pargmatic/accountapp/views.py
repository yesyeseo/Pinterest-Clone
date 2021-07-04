from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from accountapp.models import HelloWorld

# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input') 

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        # 실재로 DB에 hello world 객체를 저장하겠다는 뜻        
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # accountapp에 있는 hello world로 재접속해라 <- urls.py 

    else: # GET
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})