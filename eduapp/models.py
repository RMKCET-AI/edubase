from django.db import models
from django_summernote.fields import SummernoteTextField
from django.contrib.auth.models import User


# Create your models here.
class image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


class AI_Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "AI"


class ai_note(models.Model):
    subject = models.ForeignKey(AI_Subject, on_delete=models.CASCADE)
    note_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='ai_materials/')


class CSE_Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "CSE"


class cse_note(models.Model):
    subject = models.ForeignKey(CSE_Subject, on_delete=models.CASCADE)
    note_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='cse_materials/')


class IT_Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "IT"


class it_note(models.Model):
    subject = models.ForeignKey(IT_Subject, on_delete=models.CASCADE)
    note_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='it_materials/')


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image_template = models.ImageField(upload_to='blog_template_pics/', default='')
    tag = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog"
