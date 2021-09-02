from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
import uuid
# Create your models here.


class Category(models.Model):
    cat = models.CharField(max_length=100)
    cat_slug = models.SlugField(max_length=120)
    desc = models.TextField(max_length=100)

    def __str__(self):
        return self.cat


class PhotoStoreModel(models.Model):
    cat = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="pstore/photo/")
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class OrderFormModel(models.Model):
    orderId = models.UUIDField(
        unique=True,  default=uuid.uuid4,)
    orderfrom = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(PhotoStoreModel, on_delete=models.CASCADE)
    changeType = models.TextField(max_length=100)
    note = models.TextField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (str(self.orderfrom)+"--"+str(self.orderId))


class FormCust1Model(models.Model):
    order_from = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    photoid = models.ForeignKey(PhotoStoreModel, on_delete=models.CASCADE)
    custType = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    detail = models.TextField(max_length=200)
    note = models.CharField(max_length=100)

    # def get_img_link(self){
    #     self.photoid.
    # }

    def __str__(self):
        return str(self.order_from)
