from django.db import models


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
