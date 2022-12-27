from django.shortcuts import render

from . import util

import markdown2
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, TITLE):
    
    # Get the content written in markdown from the database. 
    content= util.get_entry(TITLE)

    if content == None:
        return render(request, "encyclopedia/pages.html", {
        "htmlBodyContent":" <h1>Error</h1> Page Not Found ",
        "TITLE":TITLE
        })
    else:
        #Convert the markdown into HTML
        html_body = markdown2.markdown( content )
        return render(request, "encyclopedia/pages.html", {
        "htmlBodyContent":html_body,
        "TITLE":TITLE
        }) 

def search(request):
    if request.method == "POST":
        # Get the Query text, the user typed in the search box.
        query = request.POST['q'].lower()
        # Get all the entries. # Below is the way to make all the list item in lowercase.
        entries= [x.lower() for x in util.list_entries()] 

        # if exact match found in the list of entries.
        if query in entries:
            return title(request,query)
        
        # if any substring (part of a string) match found 
        elif any(query in s for s in entries):
            # All the list of partial matches
            matching = [s for s in entries if query in s]
            # Capitalize the first letter of the list entry.
            matching = [m.capitalize() for m in matching]

            return render(request, "encyclopedia/search.html", {
                "matching": matching
            })
        
        # if no matches found.
        else:
            return render(request, "encyclopedia/error.html")



def createNewPage(request):
    if request.method == "POST":
        #write the function to save the content.
        vTitle = request.POST['Ntitle']
        vContent = request.POST['Ncontent']

        vTitleLower = request.POST['Ntitle'].lower()
        entries= [x.lower() for x in util.list_entries()]
        
        if vTitleLower in entries:
            return render(request, "encyclopedia/createNewPage.html",{
                "vTitle": vTitle,
                "vContent": vContent,
                "errorMessage":"This title already Exist, please try different title."
            })
        else:
            util.save_entry(vTitle, vContent)
            return title(request,vTitle)
    
    else:
        return render(request, "encyclopedia/createNewPage.html")

def editPage(request, newTitle):
    #write function to edit the page.
    if request.method == "POST":
        #to save the new content.
        vContent = request.POST['Ncontent']
        util.save_entry(newTitle, vContent)
        return title(request,newTitle)
    
    else:
        newContent = util.get_entry(newTitle)
        return render(request, "encyclopedia/editPage.html", {
            "newContent": newContent,
            "newTitle": newTitle
        })


def randomPage(request):
    entries = util.list_entries()
    randomTitle = random.choice(entries)
    return title(request,randomTitle)