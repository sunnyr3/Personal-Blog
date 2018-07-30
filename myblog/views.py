from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from .models import Post, Category, About, Project
from .forms import PostForm

def index(request):
    return render(request, 'blog/index.html')

# About
def about_list(request):
    abouts = About.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/about.html', {'abouts': abouts})

def about_detail(request, pk):
    about = get_object_or_404(About, pk=pk)
    context = {'about': about}
    return render(request, 'about/about_detail.html', context)


