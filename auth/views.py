from django.http import HttpResponse 
from django.template import loader

def index(request):
    template = loader.get_template("login.html")
    context = {
        "page_title": "Login"
    }
    return HttpResponse(template.render(context, request))

def account(request):
    template = loader.get_template("account.html")
    context = { 
        "page_title": "Account"
    }
    return HttpResponse(template.render(context, request))

