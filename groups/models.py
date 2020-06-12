from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
User=get_user_model
from djago import template
register=template.Library()
from django.urls import reverse
# Create your models here.

class Group(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
    description=models.CharField(widget=models.Textarea,default='',blank=True)
    description_html=models.CharField(widget=models.Textarea,blank=True,default="",editable=False)
    members=models.ManyToManyField(User,through="GroupMember",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering=['name']

class GroupMember(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='membership')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_groups')

    def __str__(self):
        return self.user.username
    class Meta:
        unique_together=('group','user')
