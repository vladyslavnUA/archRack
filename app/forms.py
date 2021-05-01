from django import forms
from django.contrib.auth import get_user_model
from .models import *
from django.forms import ModelForm

class CreateDocForm(forms.ModelForm):
    # """user signup form"""
    # email = forms.EmailField()
    # name = forms.CharField()
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RackDoc
        # fields = ('email', 'name', 'password1', 'password2',)
        exclude = ('created_at', 'updated_at', 'owner', 'slug')
    
    # def save(self, *args, **kwargs): 
    #     if not commit: 
    #         raise NotImplementedError("Can't create Document without database save") 
    #     doc = super().save(*args, **kwargs)
    #     doc_saved = RackDoc(name=self.cleaned_data['name'], 
    #                         project=self.cleaned_data['project'], content=self.cleaned_data['content'],
    #                         owner=self.cleaned_data['owner'],) 
    #     for i in self.cleaned_data['collaborators']:
    #         doc_saved.collaborators.add(i)
    #     doc_saved.save()
    #     return doc

class HalfDocForm(forms.ModelForm):
     class Meta:
        model = RackDoc
        exclude = ('content', 'created_at', 'updated_at', 'owner', 'slug')

class UpdateDocForm(forms.ModelForm):
    # """user signup form"""
    # email = forms.EmailField()
    # name = forms.CharField()
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RackDoc
        # fields = ('email', 'name', 'password1', 'password2',)
        exclude = ('created_at', 'updated_at', 'owner', 'slug')

class CreateProjectForm(forms.ModelForm):
    # """user signup form"""
    # email = forms.EmailField()
    # name = forms.CharField()
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('email', 'name', 'password1', 'password2',)
        exclude = ('rackdocs', 'created_at', 'updated_at', 'owner', 'slug')