
from django.urls import path
from book_app import views


urlpatterns = [
    path('details/<int:id>',views.class_vased_details.as_view(),name='details_book'),
    path("borrow/<int:id>",views.borrow,name='borrow_book'),
    path("list_borrow/",views.list_borrow_book.as_view(),name='borrow_list_book'),
    path("returnbook/<int:return_id>",views.return_book.as_view(),name='return_book')
]
