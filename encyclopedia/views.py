from django.shortcuts import render, redirect
import markdown
from . import util
import random

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message":"This entry doesnot exist!"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
    
def search(request):
    if request.method == "POST":
        entry_search = request.POST["q"]
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title":entry_search,
                "content":html_content
            })
        else:
            allentries = util.list_entries()
            recomendation=[]
            for entry in allentries:
                if entry_search.lower() in entry.lower():
                    recomendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recomendation":recomendation
            })
        
def create_entry(request):
    if request.method=="GET":
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        entry_exist = util.get_entry(title)
        if (entry_exist==None):
            util.save_entry(title, content)
            return redirect(index)
        else:
            return render(request, "encyclopedia/create.html", {
            "message":"This title already exist!"
        })

def edit_entry(request):
    if request.method=="POST":
        title = request.POST["title"]
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title":title,
            "content":entry
        })
    
def edit(request):
    if request.method=="POST":
        title = request.POST["title"]
        util.save_entry(title=title, content=request.POST["content"])
        return redirect('entry', title=title)
    
def random_entry(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return redirect('entry', title=title)