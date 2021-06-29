from django import forms

class AddUser(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a name'}))
    surname = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a surname'}))
    
class DeleteUser(forms.Form):
    id = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a id'}))

class UpdateForm(forms.Form):
    id = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a id'}))
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a new name'}))
    surname = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a new surname'}))