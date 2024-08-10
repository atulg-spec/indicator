from django.urls import path
from home.views import *
# urls.py
urlpatterns = [
    # PAGES
    path("",index,name='index'),
    path("about",about,name='about'),
    path("indicators",indicators,name='indicators'),
    path("contact",contact,name='contact'),
    path("disclaimer",disclaimer,name='disclaimer'),
    path("privacypolicy",privacypolicy,name='privacypolicy'),
    path("refundpolicy",refundpolicy,name='refundpolicy'),
    path("careers",careers,name='careers'),
]
