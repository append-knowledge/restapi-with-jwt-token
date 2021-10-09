from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from project.models import MyUser
from project import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class SignUpview(CreateView):
    model = MyUser
    form_class = forms.SignUpForm
    template_name ='project/signup.html'
    success_url = reverse_lazy('signin')

class SignInView(TemplateView):
    form_class=forms.SignInform
    template_name = 'project/signin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():

            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,username=email,password=password)
            print(user, email, password)
            if user:
                login(request,user)

                return redirect('home')
            else:
                print('no user')
                return redirect('signin')
        else:
            print('form not valid')
            return redirect('signin')


class SignOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')

class HomeView(ListView):
    model = MyUser
    template_name = 'project/home.html'
    context_object_name = 'details'

class ChangeDetailsView(UpdateView):
    model = MyUser
    form_class = forms.UserprofileForm
    template_name = 'project/update.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

def delete(request,id):
    model=MyUser
    detail=model.objects.get(id=id)
    detail.delete()
    return redirect('home')








