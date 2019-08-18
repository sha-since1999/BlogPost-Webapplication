from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template 
from .forms import ContactForm
# doc="<h1>{title}</h1>".format(title=M_title)
# django_render_doc="<h1>{{title}}</h1>".format(title=M_title)

def home_page(request):
	M_title       = "hello there"
	context       = { "title":"Example","my_list":[1,2,3,4,5,6]}
	if request.user.is_authenticated:
		context       = { "title":"Example","my_list":[1,2,3,4,5,6]}
	templete_name = "home.html"
	templete_obj  = get_template(templete_name)
	template_string = templete_obj.render(context)
	return render(request,"home.html",{"title":template_string})
	# return render(request,"home.html",{"my_list":[1,2,3,4,5,6]})

	

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	form=ContactForm()  #re initialise the form
	context={"title":'contact-us', "form": form}
	return render(request,"form.html",context)

	
def about(request):
    return render(request,"abouts.html",{"title":'home_pages_of Projects'})
def description(request):
    return HttpResponse("<h1>description</h1>")
def example(request): 
	context       = { "title":"Example"}
	templete_name = "abouts.html"
	templete_obj  = get_template(templete_name)
	return HttpResponse(templete_obj.render(context))






def form_data(request):
	d=request.POST
	data=d.copy()
	data.pop('csrfmiddlewaretoken')
    # name=request.POST['full_name:']
	print(data)
	return render(request,'form_data.html',{"data":data,'name':data['full_name:'],'email':data['email:'],'textarea':data['textarea:']})











