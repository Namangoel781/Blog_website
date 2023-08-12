from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):

    Popular_blogs = Popularblogs.objects.all()

    context = {'popularBLOGS':Popular_blogs}
    
    return render(request, 'home.html', context)

def about(request):

    return render(request, 'about.html' )

def contact(request):

    if request.method == 'POST':

        cname = request.POST['name']
        cemail = request.POST['email']
        cphone = request.POST['phone']
        caddress = request.POST['address']
        cmsg = request.POST['message']

        if len(cname)>2 and len(cemail)>10 and len(cphone)>10 and len(caddress)>5 and len(cmsg)>3:
            contactObj = ContactUsTb(name=cname, email=cemail, phone=cphone, address=caddress, message=cmsg)
            contactObj.save()

        else:
            return HttpResponse("Error in Submit")
           



    return render(request, 'contact.html')

def view_blog(request, pk):

    viewBlog = Popularblogs.objects.get(pk=pk)

    return render(request, 'viewblog.html', 
    {'viewBlog':viewBlog})