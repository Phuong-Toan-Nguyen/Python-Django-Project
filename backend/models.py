from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Menu_Items(models.Model):
    ItemName = models.CharField(max_length=20, null=False)
    Url = models.CharField( max_length=200,  null=True, blank=True)
    
class Logo_pic(models.Model):
    Img = models.ImageField(upload_to='logos/', null=True)
    Alt = models.CharField( max_length=200, null=True)

class Donors(models.Model):
    FaviconDonors = models.ImageField(upload_to='Donors/', null=True,)
    Url = models.CharField(max_length=100, null=True,)
    Alt = models.CharField( max_length=200, null=True)

def validate_carousel_id(value):
    if value not in range(1,5):
        raise ValidationError('ID must be between 1 and 4')
class Carousel_Items(models.Model):
    Carousel_id = models.IntegerField(primary_key=True, unique=True, validators=[validate_carousel_id])
    Img = models.ImageField(upload_to='carousels/', null=True)
    description = models.CharField(max_length=200, null=True)
    alt = models.CharField( max_length=200, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None: #new
            if Carousel_Items.objects.count() >= 4:
                raise ValueError("Only 4 elements allowed in this model.")
            else:
                super().save(*args, **kwargs)
        else: #update
            super().save(*args, **kwargs)
            
class News_Items(models.Model):
    Title = models.CharField(max_length=100, null=True)
    ImgThumb = models.ImageField(upload_to='news/', null=True)
    VideoUrl = models.CharField(max_length=100, null=True, blank=True)
    UpdateAt = models.DateField()
    Content = RichTextUploadingField(blank = True, null = True)
    
class OnA_Items(models.Model):
    Title = models.CharField(max_length=30,)
    Date = models.DateField(null=True)
    Detail = models.CharField(max_length=20,)
    
class Story_Items(models.Model):
    ImgThumb = models.ImageField(upload_to='story/', null=True)
    Title = models.CharField(max_length=50, null=True)
    SubTitle = models.CharField(max_length=100, null=True)
    Content = RichTextUploadingField(blank = True, null = True)
    
class Staff_Cast(models.Model):
    Img = models.ImageField(upload_to='StaffCast/', null=True,)
    Name = models.CharField(max_length=30, null=True,)
    Url = models.CharField(max_length=100, null=True,)
    Movie = models.CharField(max_length=20, null=True,)
    job = models.CharField(max_length=20, null=True,)

class Trailer(models.Model):
    Img = models.ImageField(upload_to="Trailers/", null=True,)
    Name = models.CharField(max_length=30, null=True,)
    Url = models.CharField(max_length=100, null=True,)
    
class Music(models.Model):
    Img = models.ImageField(upload_to="Musics/", null=True,)
    Name = models.CharField(max_length=50, null=True,)
    Type = models.CharField(max_length=30, null=True,)
    Content = RichTextUploadingField(blank = True, null = True)
    
class Podcast(models.Model):
    Name = models.CharField(max_length=50, null=True,)
    Img = models.ImageField(upload_to="Podcast/", null=True,)
    Url = models.CharField(max_length=100, null=True,)

class SNS(models.Model):
    Name = models.CharField(max_length=50, null=True,)
    Img = models.ImageField(upload_to="SNS/", null=True,)
    Url = models.CharField(max_length=100, null=True,)
    
class Goods(models.Model):
    Name = models.CharField(max_length=50, null=True,)
    Img = models.ImageField(upload_to="Goods/", null=True,)
    SellDate = models.CharField(max_length=50, null=True,)
    Price = models.CharField(max_length=50, null=True, blank=True)
    Category = models.CharField(max_length=30, null=True,)
    Description = models.CharField(max_length=200, null=True,)
    Url = models.CharField(max_length=100, null=True,)
    
class Category(models.Model):
    Name = models.CharField(max_length=20, null=True,)
    Description = models.CharField(max_length=200, null=True, blank=True)
    
class Contact(models.Model):
    name = models.CharField('User Name', max_length=60)
    address = models.CharField(max_length=300)
    email_address = models.EmailField('Email Address')
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    zip_code = models.CharField('Zip Code', max_length=15, blank=True)





class Something(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    
