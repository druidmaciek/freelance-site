from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from .forms import ContactForm
from .models import Post


TESTIMONIALS = [
    {
        "name": "Hugh Topping",
        "photo": static('img/testimonial1.jpeg'),
        "position": "Founder",
        "company": "crowdEngage",
        'text': 'Maciej has provided us with custom software development in support of our business. He was quick, '
                'diligent and very professional. I will definitely utilize his services in future endeavors. He is an '
                'expert Python developer who is a pleasure to work with. '
    },
    {
        "name": "Doron Grinstein",
        "photo": static('img/testimonial2.jpg'),
        "position": "CEO",
        "company": "Buywiser",
        'text': 'Maciej has provided us with custom software development in support of our business. He was quick, '
                'diligent and very professional. I will definitely utilize his services in future endeavors. He is an '
                'expert Python developer who is a pleasure to work with. '
    },
    {
        "name": "Karol Zakrzewski",
        "photo": static('img/testimonial3.png'),
        "logo": static('svg/logo_tv.svg'),
        "position": "CEO",
        "company": "Televisor",
        'text': 'Maciej has provided us with custom software development in support of our business. He was quick, '
                'diligent and very professional. I will definitely utilize his services in future endeavors. He is an '
                'expert Python developer who is a pleasure to work with. '
    },
]


def home(request):
    return render(request, 'home/home.html', {
        'testimonials': TESTIMONIALS,
        'section': 'home',
    })


class PostList(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/list.html"
    #TODO add published manager to queryset


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'


@require_POST
def contact_form(request):
    form = ContactForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Contact Request Sent, I will get back to you in next few days')
    else:
        messages.error(request,
                       'There was an error when saving contact form. Send me an email instead! '
                       '<b>maciej@janowski.dev</b>.')
    return redirect(reverse('home'))

