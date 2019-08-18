from django import forms
from .models import BlogPost



class BlogPostForm(forms.Form):
    title   =forms.CharField()
    slug    =forms.SlugField()
    img     =forms.ImageField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    title=forms.CharField(max_length=120) #here we modify the field  and type  of BlogPost model
    class Meta:
        model:BlogPost
        field:['title','img','slug','content']   #field:"__all__"
    
    # title validation customisation
    def clean_title(self,*args,**kwargs):
        instance=self.instance
        title=self.cleaned_data.get('title')
        qs=BlogPost.objects.filter(title=title)       #title_icontais  or # title_iexact   its  means on using lowercase t give erorr
          
        #just if u  want dont update any hting than u can do this  
        if instance is not None:
            qs=qs.exclude(pk=instance.pk) #id==intance.id
         

        if qs.exists():
            raise forms.ValidationErorr("this title is already exist please try again")
        return title

    #this title validation also can be given by using unique argument to fiel model  


    def clean_email():
        email=self.cleaned_data.get('email')
        if email.endswith(".edu"):
            raise forms.ValidationErorr("this is envail")
        return eamil