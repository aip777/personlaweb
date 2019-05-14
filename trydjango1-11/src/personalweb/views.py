from django.shortcuts import render
import random

from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import PersonalWebsite
# Create your views here.

from .models import Post, Recentwork, Gallery, Experience, Education, Skill, Services, Client
from django.utils import timezone
from django.shortcuts import render , get_object_or_404


# email import

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EmailCreateForm

# end email import
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect



# def restaurants_list_view(request):
#     template_name ="restaurants/restaurantslocation_list.html"
#     queryset = RestaurantsLocation.objects.all()
#     context ={
#         "object_list":queryset
#     }
#
#     return render(request, template_name, context)



















# class HomeView(TemplateView):
#    template_name = "home.html"
#
#    def get_context_data(self,*args ,**kwargs):
#
#        context = super(HomeView,self).get_context_data(*args, **kwargs)
#
#        num = None
#        some_list = [random.randint(1, 1000),
#                     random.randint(1, 1000),
#                     random.randint(1, 1000)
#                     ]
#        condition_bool_item = True
#        if condition_bool_item:
#            num = random.randint(1, 1000)
#
#        context = {
#            "bool_item": True,
#            "num": num,
#            "some_list": some_list
#        }
#        return context







# class AboutView(TemplateView):
#    template_name = "about.html"
#
#
#
#
#
# class ContactView(TemplateView):
#    template_name = "index.html"


#
# class WebView(TemplateView):
#    template_name = "index.html"





def index_list_view(request):
    template_name ="index.html"
    queryset = PersonalWebsite.objects.all()
    post_queryset = Post.objects.all()
    recentwork = Recentwork.objects.all()
    gallery_post = Gallery.objects.all()
    experience_post = Experience.objects.all()
    education = Education.objects.all()
    skill = Skill.objects.all()
    services = Services.objects.all()
    client = Client.objects.all()

    paginator = Paginator(gallery_post, 3)
    page = request.GET.get('page')

    # paginator_post = Paginator(post_queryset, 6)
    # page_post = request.GET.get('pa')

    # Handle out of range and invalid page numbers:
    try:
        gallery_post_new = paginator.page(page)
    except PageNotAnInteger:
        gallery_post_new = paginator.page(1)
    except EmptyPage:
        gallery_post_new = paginator.page(paginator.num_pages)

    # try:
    #     post_queryset_new = paginator_post.page(page_post)
    # except PageNotAnInteger:
    #     post_queryset_new = paginator_post.page(1)
    # except EmptyPage:
    #     post_queryset_new = paginator_post.page(paginator_post.num_pages)

    # start email
    form = EmailCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    if form.errors:


        errors = form.errors


    # end email send





    context ={
        "object_list":queryset,
        "post_queryset_new":post_queryset,
        "object_list_recentwork":recentwork,
        "gallery_post_new":gallery_post_new,
        "gallery_post":gallery_post,
        "form":form,
        "experience_post":experience_post,
        "education":education,
        "skill":skill,
        "services":services,
        "client":client,
    }

    return render(request, template_name, context)





#
# def index_list_view_new(request):
#     template_name ="html/blog-new.html"
#     queryset = Post.objects.all()
#     context ={
#         "object_list":queryset
#     }
#
#     return render (request, template_name, context)










