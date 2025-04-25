from django import forms

from .models import Items 

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Items 
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category' : forms.Select(attrs={
                'class': INPUT_CLASSES,  # Specific class for dropdown,
            }),
            'name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description' : forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price' : forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image' : forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Items 
        fields = ('name', 'description', 'price', 'image','is_sold')
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description' : forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price' : forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image' : forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'is_sold' : forms.CheckboxInput(attrs={
                'class': "mt-5 h-5 w-5 text-purple-600 transition duration-150 ease-in-out rounded focus:ring-2 focus:ring-purple-400 focus:outline-none",
            }),
        } 

