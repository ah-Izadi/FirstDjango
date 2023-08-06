from django.urls import path
from .views import index,detail,detailEmail

urlpatterns = [
    path('',index),
    path('<int:MovieID>',detail),
    path('SendEmail/<to>',detailEmail)
]
