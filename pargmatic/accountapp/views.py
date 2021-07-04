from django.http import HttpResponse
from django.shortcuts import render
from accountapp.models import HelloWorld

# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input') 

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # 실재로 DB에 hello world 객체를 저장하겠다는 뜻        
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
        # 객체를 내보내 줌

    else: # GET
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})