from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    # reverse는 class에서 사용할 수 없다. reverse_lazy를 class에서 사용함.
    # 기능은 별로 차이가 없음
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'