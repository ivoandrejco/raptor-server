from django.shortcuts import render

# Create your views here.
def notFound(request):
    return HttpResponse("not found",status=404)
