from django.shortcuts import render
from django.http import HttpResponse
from . import util

"""class NewTaskForm(forms.Form):
    task = forms.CharField()"""

def index(request):
    if request.GET:
        query = request.GET["q"]
        if query in util.list_entries():
            return render(request, "encyclopedia/get_entry.html", {
                "entry": util.get_entry(query)
            })
        
        else:
            similar_entries = []
            for entry in util.list_entries():
                if query.upper() in entry.upper():
                    similar_entries.append(entry)

            return render(request, "encyclopedia/search_results.html", {
                "query": query,
                "similar_entries": similar_entries
            })
    else:
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
