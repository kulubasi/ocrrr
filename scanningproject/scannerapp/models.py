from django.db import models

# Create your models here.
class myimages(models.Model):
    # title=models.CharField(max_length=100)
    # author=models.CharField(max_length=100)
    # pdf=models.FileField(upload_to='books/pdf/')
    img=models.ImageField(upload_to='imagegallery/')
    #cover=ResizedImageField(size=[500,300],upload_to='books/covers/',null=True,blank=True)

    def __str__(self):
        return self.title
        #return self.caption


class mypdfs(models.Model):
    # title=models.CharField(max_length=100)
    # author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='pdfs/')
    # img=models.ImageField(upload_to='imagegallery/')
    #cover=ResizedImageField(size=[500,300],upload_to='books/covers/',null=True,blank=True)

    def __str__(self):
        return self.title
        #return self.caption