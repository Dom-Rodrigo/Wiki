from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import util

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
    print(query)
    if query in util.list_entries():
        return render(request, "encyclopedia/get_entry.html", {
            "entry": util.get_entry(query),
            "query": query,
        })
    
    else:
        return HttpResponse("404: Not found")

def new_page(request):
    if request.POST:
        title = request.POST["title"]
        markdown = request.POST["markdown"]
        if title in util.list_entries():
            return HttpResponse(f"Page {title} already exists")
        else:
            util.save_entry(title, markdown)
            return redirect("encyclopedia:get_entry", f"{title}")

        return render(request, "encyclopedia/new_page.html")

    else:
        return render(request, "encyclopedia/new_page.html")

def edit(request, query):
    old_title = query
    old_markdown = util.get_entry(query)
    if request.POST:
        title = request.POST["title"]
        markdown = request.POST["markdown"]
        util.save_entry(title, markdown)
        util.delete_entry(old_title)

        return redirect("encyclopedia:get_entry",  f"{title}")

    return render(request, "encyclopedia/edit.html", {
        'old_title': old_title,
        'old_markdown': old_markdown
    })
