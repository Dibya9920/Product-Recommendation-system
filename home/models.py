from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name 



class ScrappedProduct(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    rating = models.FloatField()
    link = models.ImageField( upload_to='image', default='link')
    price = models.CharField(max_length=50, null=True)
    dprice = models.CharField(max_length=50, null=True)
    perdis = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.title
    

class Search(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    rating = models.FloatField()


    def __str__(self):
        return self.title