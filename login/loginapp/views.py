from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogpost
from django.http import Http404
from .forms import BlogPostModelForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.
# def home(request):
#     context = {'title' : 'Blog','mylist' : [1,2,3,4]}
#     return render(request, 'home.html', context)

# def blog_post_detail_page(request, post_id):
#     try:
#         obj = Blogpost.objects.get(id=post_id)
#     except:
#         raise Http404
#     template_name = 'blog_post_detail_page.html'
#     context = {"object":obj}
#     return render(request, template_name, context)


# def blog_post_detail_page(request, post_id):
#     obj = get_object_or_404(Blogpost, id = post_id)
#     template_name = 'blog_post_detail_page.html'
#     context = {"object":obj}
#     return render(request, template_name, context)

# def blog_post_detail_page(request, slug):
#     obj = get_object_or_404(Blogpost, slug=slug)
#     template_name = 'blog_post_detail_page.html'
#     context = {"object":obj}
#     return render(request, template_name, context)

# def blog_post_detail_page(request, slug):
#     querryset = Blogpost.objects.filter(slug=slug)
#     if querryset.count() != 1:
#         raise Http404
#     else:
#         obj = querryset.first()
#     template_name = 'blog_post_detail_page.html'
#     context = {"object":obj}
#     return render(request, template_name, context)

# def blog_post_detail_page(request, slug):
#     querryset = Blogpost.objects.filter(slug=slug)
#     if querryset.count() >= 1:
#         obj = querryset.first()
#     template_name = 'blog_post_detail_page.html'
#     context = {"object":obj}
#     return render(request, template_name, context)

# CRUD

# GET -> Retrieve / List

# POST -> Create / Update / Delete

# Create Retrieve Update Delete

def blog_post_list_view(request):
    # list out objects
    # could be search 
    # qs = Blogpost.objects.filter(title__icontains="hello")
    
    now = timezone.now()
    qs = Blogpost.objects.filter(publish_date__lte=now)
    if request.user.is_authenticated:
        my_qs = Blogpost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog_post_list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

@login_required
def blog_post_create_view(request):
    # method 1
    # form = BlogPostForm(request.POST or None)
    
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        
        # Manipulating some data of the form before saving it 
        # obj.save(commit=False)
        # obj.title = form.cleaned_data.get("title") + "0"
        # obj.save()

        # obj = Blogpost()
        # obj.title = form.cleaned_data['title']
        # obj.slug = form.cleaned_data['slug']
        # obj.content = form.cleaned_data['content']
        # obj.save()
        # shortcut is below

        # method 1 
        # obj = Blogpost.objects.create(**form.cleaned_data)
        
        # method 2
        now = timezone.now()
        obj = form.save(commit=False)
        obj.user = request.user
        if obj.publish_date:
            obj.publish_date = now
            print(now)
            print(obj.publish_date)
        obj.save()

        # form.save() without the user associated to the post
        form = BlogPostModelForm() # reinitializing a form
    template_name = 'blog_post_create.html'
    context = {'form':form, 'title':"Create New Post"}
    return render(request, template_name, context)

def blog_post_detail_view(request,slug):
    obj = get_object_or_404(Blogpost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {'object':obj}
    return render(request, template_name, context) 

@login_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(Blogpost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/blog/'+obj.slug)
    template_name = 'blog_post_create.html'
    context = {'form':form, "title":f"Update {obj.title}"}
    return render(request, template_name, context)

@login_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(Blogpost, slug=slug)
    template_name = 'blog_post_delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {'object':obj}
    return render(request, template_name, context)