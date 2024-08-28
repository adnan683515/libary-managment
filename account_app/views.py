from django.shortcuts import render,redirect
from django.views.generic import FormView
from account_app.forms import user_register_form,Deposit_form
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from account_app.models import Account
from django.views.generic import CreateView, ListView,FormView
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class register_view(CreateView):
    model = User
    template_name = 'register.html'
    form_class = user_register_form
    success_url = reverse_lazy('log_in')
    
    def form_valid(self,form):
        # form.save()
        messages.success(self.request,f"Account Created Successfully!.")
        return super().form_valid(form)
       
    
    
    
class log_in_view(LoginView):
    template_name = 'register.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'loged in successfull!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,f'Your loged in information incorrect')
        return super().form_invalid(form)
    
    
   
def log_OUt(request):
    logout(request)
    return redirect('log_in')
   
      
class Deposit_view(LoginRequiredMixin,FormView):
    
   
    
    def get(self, request, *args, **kwargs):
        form = Deposit_form()
        return render(request,'deposit.html',{"form":form,'title':'Deposit Form','account':self.request.user.user_account})
    
    def post(self, request, *args, **kwargs): 
        if self.request.method == "POST":
            form = Deposit_form(self.request.POST)
            if form.is_valid():
                amount = form.cleaned_data.get('balance')
                print(amount)
                
                 
                obj = Account.objects.get(account_no=self.request.user.user_account.account_no)
                obj.balance = obj.balance + amount
                obj.balance_after_tranjections = obj.balance
                obj.save()
                
                                
                mail_subject = "Deposit Messages"
                message = render_to_string('depositmsg.html',{
                    'user':self.request.user,
                    'amount':amount,
                    'nowbalance':self.request.user.user_account.balance + amount

                }) 
                to_email = self.request.user.email 
                send_email = EmailMultiAlternatives(mail_subject," ",to=[to_email])
                send_email.attach_alternative(message,'text/html')
                send_email.send()
                
                messages.success(self.request,f"Successfully {amount}tk Deposit Done.")
                return redirect('deposit')
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Deposit Form' 
        return context
        
    
    

    
# class Deposit_view(CreateView):
#     template_name = 'deposit.html'
#     form_class = Deposit_form
#     success_url = reverse_lazy('deposit')
#     model = Account
#     title = 'Deposit Form '
    
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({
    #         'account': self.request.user.user_account
            
    #     })
    #     return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = self.title
    #     return context

    
    # def form_valid(self,form):
    #     amount = form.cleaned_data.get('balance')
    #     obj = Account.objects.get(account_no=self.request.user.user_account.account_no)
    #     print(obj.balance)
        
    #     return super().form_valid(form)
    