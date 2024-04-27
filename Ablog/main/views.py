from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from .models import CreateBlog, images


# home page view

class Homepage(ListView):
    model = CreateBlog
    template_name = "main/template/home.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = images.objects.all()
        return context


# blog page view
class Blogpage(DetailView):
    model = CreateBlog
    template_name = "main/template/blog.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = images.objects.all()
        return context


# read more view
def show(request):
    return render(request, "main/template/blog.html")


# admin dashboard------------------------------------------------------------------------------------
def admindashboard(request):
    if request.method == 'POST':
        grab_title = request.POST['title']
        grab_Summary = request.POST['Summary']
        grab_author = User.objects.get()

        grab_title_tag = request.POST['title_tag']
        grab_content = request.POST['content']

        new_blog_post = CreateBlog(
            title=grab_title,
            author=grab_author,
            title_tag=grab_title_tag,
            body=grab_content,
            Summary=grab_Summary

        )
        new_blog_post.save()

    return render(request, "main/template/admin1.html")


# choose post view

class updatepost_view1(ListView):
    model = CreateBlog
    template_name = "main/template/choose_blog.html"
    context_object_name = "post"


def edit_blog(request, pk):
    post = get_object_or_404(CreateBlog, id=pk)

    if request.method == 'POST':
        post.title = request.POST['title']

        post.title_tag = request.POST['title_tag']
        post.body = request.POST['content']
        post.save()
        return redirect('home')  # Redirect to homepage after successful edit

    context = {'post': post}

    return render(request, "main/template/update_blog.html", context)


def delete(request, pk):
    post = CreateBlog.objects.get(id=pk)

    post.delete()
    return redirect('adminurl')
    # context = {'post': post}
# return render(request,"main/template/choose_blog.html")
