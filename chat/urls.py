
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('<slug:slug>/' , views.chatroom , name='chatroom'),
    path('edit_room/<slug:slug>/' , views.edit_room , name='edit_room'),
    path('delete_room/<slug:slug>/' , views.delete_room , name='delete_room'),

]