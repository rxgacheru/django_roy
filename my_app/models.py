from django.db import models
from django.urls import reverse
from django import forms


class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  

  def get_absolute_url(self):
    return reverse('author-details', args=[str(self.id)])
  
  def __str__(self):
    return f'{self.first_name} {self.last_name}'
   
# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  content = models.TextField(max_length=5000)
  created_date = models.DateTimeField(auto_now_add=True)
  published_date = models.DateTimeField(auto_now_add=False)

  def __str__(self):
    return self.title
  
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class BlogForm(forms.ModelForm):
    # Define the author field as a dropdown menu of authors
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select an author")

    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'is_published']

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # Customize the form's appearance or behavior here if needed

    def clean(self):
        cleaned_data = super().clean()
        # Additional form validation can be performed here
        return cleaned_data