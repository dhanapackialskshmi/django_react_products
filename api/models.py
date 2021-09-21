from django.db import models

# Create your models here.
#from django.contrib.postgres.fields import ArrayField


class Basetable(models.Model):
    base_id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
   

class Properties(models.Model):
    product_id = models.AutoField(primary_key=True)
    original_price = models.IntegerField()
    price = models.IntegerField()
    base = models.ForeignKey(Basetable, on_delete=models.CASCADE)
    #base_id = models.ForeignKey("Basetable", related_name="Properties", on_delete=models.CASCADE)
    


 
class Dimensions(models.Model):
    id = models.AutoField(primary_key=True)
    length = models.DecimalField(max_digits=7,decimal_places=2)
    width = models.DecimalField(max_digits=7,decimal_places=2)
    height = models.DecimalField(max_digits=7,decimal_places=2)
    base= models.ForeignKey(Basetable, on_delete=models.CASCADE)
    product = models.ForeignKey(Properties, on_delete=models.CASCADE)


class Images(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_listimage = models.BooleanField(default=True)
    url = models.URLField(max_length=100)
   
    base= models.ForeignKey(Basetable, on_delete=models.CASCADE)
    product = models.ForeignKey(Properties, on_delete=models.CASCADE)
    
class Product(models.Model):

    product_id=models.AutoField(primary_key=True)
    productname=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    original_price=models.IntegerField()
    price=models.IntegerField()
    image_name=models.CharField(max_length=255)
    is_listimage=models.BooleanField(default=True)
    url=models.URLField(max_length=255)
























