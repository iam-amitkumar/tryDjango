from django import forms

from .models import Product


class ProductForm(forms.Form):
    title = forms.CharField(label="Title ", widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    # to give placeholder
    # email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={"placeholder": "Your emailId"}))
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 5,
                "cols": 100
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    summary = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Your Summary", "rows": 5, "cols": 100}))
    featured = forms.BooleanField(initial=False, required=False)

    # validation for fields
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "amit" in title:
    #         raise forms.ValidationError("Please provide amit in your title")
    #     return title
