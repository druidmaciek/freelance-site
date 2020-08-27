from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.PostList.as_view(),
         name='post-list'),
    path('sendForm/', views.contact_form,
         name='contact-form'),
]
