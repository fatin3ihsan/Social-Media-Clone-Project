from django.db import models
from django.urls import reverse
import misaka
from groups.model import Group
from django.contrib.auth import get_user_model
User=get_user_model()
from django.conf import settings
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at=models.DateTimeField(auto_now=True)
    message=models.CharField(widget=models.Textarea)
    message_html=models.CharField(widget=models.Textarea,editable=False)
    group=models.ForeignKey(Group,related_name='posts',blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts':single,kwargs={'username':self.user.username,
                                             'pk':self.pk})
    class Meta:
        ordering=['-created_at']
        unique_together=['user','message']
