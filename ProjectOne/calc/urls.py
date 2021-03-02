from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('add',views.add, name = 'add')

]

# To define a new path for a Page:
# In calc.urls.py   ==>>  path('calc', views.home, name = 'home'),
# 
# In project.urls.py  ==>>  path('',include('calc.urls')),
# 
# 