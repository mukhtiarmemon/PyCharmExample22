from django.http import HttpResponse

#create function for the view
def index(request):
    return HttpResponse("Hello .. This is the Polls App")
