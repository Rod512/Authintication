from django import forms

class regForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput)
    retype_pass = forms.CharField(widget= forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']
        rvalpwd = self.cleaned_data['retype_pass']
        
        if valpwd != rvalpwd:
            raise forms.ValidationError("password dosen't match")
        
class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput)
    



