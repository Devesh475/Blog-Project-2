from django.shortcuts import render
from .models import SearchQuery
from django.views.decorators.csrf import csrf_exempt
from loginapp.models import Blogpost
# Create your views here.

@csrf_exempt
def search_view(request):
    query = request.GET.get('q',None)
    user = None
    print(query)
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        qs = Blogpost.objects.filter(title__icontains=query)
    context = {"query":query, 'qs':qs}
    return render(request, 'view.html', context)