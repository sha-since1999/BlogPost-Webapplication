from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from django.contrib.auth.models import User,auth


from django.contrib import messages
from django.http import  HttpResponse,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.conf import settings
# import os
# Create your views here.
from .models import BlogPost

from .forms import BlogPostForm,BlogPostModelForm


# def upload(request):
#     if request.POST:
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render_to_response('project/upload_successful.html')
#     else:
#         form = FileForm()
#     args = {}
#     args.update(csrf(request))
#     args['form'] = form

#     return render_to_response('project/create.html', args)


# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, 'file')
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404




def blog_post_detail_page(request,slug):
    print(slug.__class__)
    print("django says",request.method,request.path,request.user)



    querryset=BlogPost.objects.filter(slug=slug)

    if querryset.count()>=1:
        obj=querryset.first()
        

    try:
        obj=BlogPost.objects.get(slug=slug)
        # obj=get_object_or_404(BlogPost,slug)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    template_name='blog/detail.html'
    context ={"object":obj ,"title":"details"}
    return render(request,template_name,context)



#CRUD
#GET-> retrieve/list
#POST-> create /update/delete
#create retrieve update delete

def blog_post_list_view(request):
    #list out the object
    #could be search 
    # qs =BlogPost.objects.all()      #objects.filter(title_icontains='hello')
    if request.user.is_authenticated:
        my_qs=BlogPost.objects.filter(user=request.user)
        # qs=(qs|my_qs).distinct()

    template_name='blog/list.html'
    context ={"object_list":my_qs,"title":"post views"}
    return render(request,template_name,context)




@login_required  #use this only if u have permanently changed
#@login_required (login_url='/login')         #means to use create we have to login first   and its arument return u at login page this also can be change in stting permanently 
# @staff_member_required   #this also maybe use to more prevent from staff member
def blog_post_create_view(request):
    #create a obejct
    #? use a form
    #request.user -> return something
    """#its the alternative method if you dont want use the decorator
    if not request.user.is_suthenticated:
        return render(requeset,"not_a_user.html" ,{})
#     """
# <<<< in this method we have to save data into my models>>>>  i have to swap the content for the get rid of indentation error

    form=BlogPostModelForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        # obj=BlogPost.objects.create(**form.cleaned_data)
        form=BlogPostModelForm()
    template_name="blog/create.html"    
    context ={"form":form}
    return render(request,template_name,context)

# <<<< in this method we have to save data into my models>>>>




        #form.save()  # firstly after storing data in form save it 
        # obj=form.save(commit=False)        #here we hold the saving of data 
        # obj.user=request.user
        # obj.title=form.cleaned_data.get('title')+"sahu"   #here we do some addition and changes on data
        # obj.save()   #and here finally we save data
        # print(form.cleaned_data)
  #   title =form.cleaned_data['title']

"""here we pass dictionary of value as argument that is break 
 by ** (for unpacking of ditionary) into key and value pair after that he looks like this
 obj=BlogPost.objects.create('title':title,'slug':slug,'content':content)
"""
"""
obj=BlogPOstForm()
obj.title=title
obj.save()
this is the another python mthod and
""" 
# again do some changes here
"""
now we create a model of models so here we can use main BlogPostModelForm)
"""




#<<<another way there is inbuild model form model, data automatically save to the given model>>>

    # form=BlogPostForm(request.POST or None);
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     obj=BlogPostForm.objects.create(**form.cleaned_data)
    #     form=BlogPostForm()
    #     #again initialise it for new objects creation
    # template_name="blog/create.html"    
    # context ={"form":form}
    # return render(request,template_name,context)


# <<<another way there is inbuild model form model, data automatically save to the given model>>>
 

@login_required 
# @staff_member_required
def blog_post_update_view(request,slug):
    obj=get_object_or_404(BlogPost,slug=slug)
    form=BlogPostModelForm(request.POST or None,request.FILES or None,instance=obj)
    if form.is_valid():
        # form.save()
        # objs=BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()

        # obj=objs
        return redirect('/blog')
    template_name='blog/update.html'
    context ={ "title":f"update {obj.title}" , "form":form }
    return render(request,template_name,context)

 
@staff_member_required
def blog_post_delete_view(request,slug):
    obj=get_object_or_404(BlogPost,slug=slug)
    if request.method=="POST":
        obj.delete()
        return redirect('/blog')
    template_name='blog/delete.html'
    context ={"object":obj,}
    return render(request,template_name,context)









# Create your views here.
def registrationBlog(request):
    if request.method == 'POST':
        print("request method is POST")
        if request.POST['username']=='' or request.POST['email']=='' or request.POST['password1']=='' or request.POST['first_name']=='':
            messages.info(request,"please fill details correctly")
            return redirect('/blog/register')
        
        first_name=request.POST['first_name']
        last_name =request.POST['last_name']
        username  =request.POST['username']
        email     =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        if password1==password2 :
            if User.objects.filter(username=username).exists():
                
                messages.info(request,"username_already_exist")
                print("username_already_exist")
                return redirect('/blog/register')

            
            elif User.objects.filter(email=email).exists():
                
                messages.info(request,'Already_registered_email')
                print("Already_registered_email")
                return redirect('blog/register')

            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                user=auth.authenticate(username=username,password=password1)
                print("save everything")
                auth.login(request,user)
                return redirect('/blog')

                
            
        else:
            messages.info(request,'password not match')
            print("password not matched")
            return redirect('/blog/register')
        return redirect('/blog')
        
    else:
        print("request is not POST method")
        return render(request,"registerBlog.html")



def loginBlog(request):
    print(request.method)
    if request.method=='POST':
        print(request.method)
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("login attempt")
            return redirect('/blog')

        else:
            messages.info(request,'invailid username/password')
            print("invailid username/password")
            return redirect('/blog/login')
    else:
        print("get_methodhas been uses")
        return render(request,"loginBlog.html")


def logoutBlog(request):
    print(request.method)
    auth.logout(request)
    return redirect('/blog')
   
