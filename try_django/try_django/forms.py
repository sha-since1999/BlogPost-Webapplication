from django import forms

class ContactForm(forms.Form):
    full_name  = forms.CharField()
    email      = forms.EmailField()
    content    = forms.CharField(widget=forms.Textarea)
    

#custom email validation
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationErorr("this is not valid email please fill again ")
        return email