from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request, query):
    if query in util.list_entries():
        return render(request, "encyclopedia/get_entry.html", {
            "entry": util.get_entry(query)
        })
    
    else:
        return HttpResponse("404: Not found")
