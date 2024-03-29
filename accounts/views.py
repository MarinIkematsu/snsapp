from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from .forms import SignInForm #SignUpForm, 
from .models import CustomUser
from django.views.generic import CreateView, TemplateView, FormView

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('snsapp:home'))
    return render(request, 'accounts/index.html')


# サインアップ
class SignUpView(CreateView):
    #form_class = SignUpForm
    model = CustomUser
    fields = ("username","email","password")
    template_name = "accounts/signup.html"
    # success_url = reverse_lazy('snsapp:home')
    success_url = reverse_lazy('accounts:index')

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password2 = request.POST['password']
        password = make_password(password2)
        user = CustomUser(username=username, email=email, password=password)
        user.save()
        login(self.request, user)
        return HttpResponseRedirect(reverse('snsapp:home'))

# サインイン（ログイン）
class SignInView(FormView):
    template_name = 'accounts/signin.html'
    form_class = SignInForm
    success_url = reverse_lazy('snsapp:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request=self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

# サインアウト（ログアウト）
def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:index')
    return render(request, 'accounts/signout.html')
