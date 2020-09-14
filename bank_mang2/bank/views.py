from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,
                                  ListView,DetailView,CreateView,UpdateView,DeleteView)
from .forms import AccountProfileForm, Amount
from .models import Account
from django.urls import reverse_lazy

# Create your views here.
class index(TemplateView):
    template_name='bank/index.html'

class about(TemplateView):
    template_name='bank/about.html'

class users_list(ListView):
    model=Account

class users_detail(DetailView):
    model=Account

class users_create(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='bank/users_list.html'
    form_class=AccountProfileForm
    model=Account

class users_update(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='bank/users_list.html'
    form_class=AccountProfileForm
    model=Account

class users_delete(LoginRequiredMixin,DeleteView):
    model=Account
    success_url=reverse_lazy('account_list')

@login_required
def deposit(request,pk):
    if request.user.is_superuser:
        obj=get_object_or_404(Account,pk=pk)
    else:
        obj=get_object_or_404(Account,pk=pk,user=request.user)

    form=Amount()
    if request.method == 'POST':
        form=Amount(request.POST)
        if form.is_valid():
            a=form.cleaned_data['value']
            b=a+obj.balance
            obj.balance=b
            obj.save()
            return redirect('account_list')
    return render(request,'bank/deposit.html',{'form':form})

@login_required
def withdraw(request,pk):
    if request.user.is_superuser:
        obj=get_object_or_404(Account,pk=pk)
    else:
        obj=get_object_or_404(Account,pk=pk,user=request.user)

    form=Amount()
    if request.method == 'POST':
        form=Amount(request.POST)
        if form.is_valid():
            a=form.cleaned_data['value']
            if a <= obj.balance:
                b=obj.balance-a
                obj.balance=b
                obj.save()

            return redirect('account_list')
    return render(request,'bank/withdraw.html',{'form':form})
