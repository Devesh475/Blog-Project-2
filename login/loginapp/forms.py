from django import forms
from .models import Blogpost, CommentForm

# Method 1 to create an object of form and then save it in views
# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)

# Method 2
class BlogPostModelForm(forms.ModelForm):
    # title = forms.CharField() if want to change the form rather than model
    class Meta:
        model = Blogpost
        fields = ['title','image','slug','content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
                                    # __iexact compares regardless of case sensitivity
        instance = self.instance 
        qs = Blogpost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Title already exist modify it slightly")
        return title

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = ['name', 'text']