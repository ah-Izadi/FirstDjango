from django.urls import path
from .views import index,detail,detailEmail

urlpatterns = [
    path('',index, name='index'),
    path('<int:MovieID>',detail, name='detail'),
    path('SendEmail/<to>',detailEmail, name='detailEmail'),
]
