from django.shortcuts import render,redirect
from django.views.generic import DetailView
from book_app.models import Book,borrow_book
from account_app.models import Account
from django.views.generic import ListView
from django.views import View
from .forms import commentFormBook
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from book_app.models import comment
# Create your views here.
class class_vased_details(DetailView):
    model = Book
    template_name = 'details.html'
    pk_url_kwarg = 'id'
    
    def post(self,request,*args, **kwargs):
        cmt_form = commentFormBook(self.request.POST)
        bk = self.get_object()
        
        if cmt_form.is_valid():
            new_form = cmt_form.save(commit=False)
            new_form.book = bk
            new_form.save()
        return self.get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bk = self.object
        cmts = bk.comments.all()
        
        context['cmts'] = cmts
        context["comment_form"] = commentFormBook
        return context
    



def borrow(request,id):
    
    borrowBook = Book.objects.get(pk=id)
    user = Account.objects.get(user=request.user)
    print(user.balance)
    print(borrowBook.quantity)
    
    if user.balance >= borrowBook.price and borrowBook.quantity != 0 and user is not None:
        user.balance = user.balance - borrowBook.price
        user.balance_after_tranjections = user.balance - borrowBook.price
        borrowBook.quantity = borrowBook.quantity - 1
        
        user.save()
        borrowBook.save()
        borrow_book.objects.create(
            user = request.user,
            buy_book= borrowBook,
    
        )
        msg_subject = "Borrow Book"
        msg_body = render_to_string('borrow_msg.html',{
            
            'book': borrowBook.title,
            'balance':request.user.user_account.balance ,
            'price':borrowBook.price,
            'user':request.user,
            'date':borrow_book.date,
        })
        
        to_email = request.user.email
        send_email = EmailMultiAlternatives(msg_subject,'',to=[to_email])
        send_email.attach_alternative(msg_body,'text/html')
        send_email.send()
        
        messages.success(request,'Successfully! check your Email.')

            
        return redirect('homepage')
    else:
        messages.warning(request,f'Sorry!.Your Balance is low.You cannot Borrow Now')
        return redirect("deposit")
        
    return redirect("homepage")
    
    
class list_borrow_book(LoginRequiredMixin,ListView):
    model = borrow_book
    template_name = 'borrow_book.html'
    context_object_name = 'borrow'
    
    def get_queryset(self):
        queryset = borrow_book.objects.filter(user=self.request.user)
        # print(queryset)
        return queryset
    
    def get_context_data(self, **kwargs):
        user = Account.objects.get(user=self.request.user)
        total_book_borrow = borrow_book.objects.filter(user=self.request.user)
        sum = 0
        for i in total_book_borrow:
            sum += i.buy_book.price
        print(sum) 
        context = super().get_context_data(**kwargs)
        context["balance"] = user.balance_after_tranjections
        context['profile'] = user
        context['total_amount'] = sum
        
        return context
    
        


class return_book(LoginRequiredMixin, View):
    def get(self,request,return_id):
        user = Account.objects.get(user=self.request.user)
        
        
        obj = borrow_book.objects.get(id=return_id)
        user.balance += obj.buy_book.price
    
        obj.buy_book.quantity += 1
        
        obj.buy_book.save()
        user.save()
        
        obj.delete()
        return redirect('borrow_list_book')
    
    
    