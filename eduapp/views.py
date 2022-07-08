import os
from django.shortcuts import render
from .models import AI_Subject,IT_Subject,CSE_Subject,BlogPost
from django.core.paginator import Paginator
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'eduapp/index.html')


def blog(request):
    blogs = BlogPost.objects.all()
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('blog_page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'eduapp/blog.html' , {'page_obj': page_obj})


def material(request):
    return render(request, 'eduapp/material.html')


def ai(request):
    ai_subjects = AI_Subject.objects.all()
    return render(request, 'eduapp/ai.html', {'ai_subjects': ai_subjects,'base_url':settings.MEDIA_URL})


def cse(request):
    cse_subjects = CSE_Subject.objects.all()
    return render(request, 'eduapp/cse.html',{'cse_subjects': cse_subjects,'base_url':settings.MEDIA_URL})


def ece(request):
    return render(request, 'eduapp/ece.html')


def mech(request):
    return render(request, 'eduapp/mech.html')

def it(request):
    it_subjects = IT_Subject.objects.all()
    return render(request, 'eduapp/it.html',{'it_subjects': it_subjects})

def blog_detail(request,blog_id):
    curr_blog = BlogPost.objects.get(id=blog_id)
    return render(request, 'eduapp/blog_detail.html', {'blog': curr_blog})