from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50,blank=True,null=True)
    last_name=models.CharField(max_length=50,blank=True,null=True)
    location=models.CharField(max_length=50,blank=True,null=True)
    url=models.CharField(max_length=50,blank=True,null=True)
    picture=models.ImageField(upload_to='profile_picture',blank=True,null=True,verbose_name='profile_picture')
    profile_info=models.TextField(max_length=256,blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    #favorites=models.ManyToManyField(Post)
    
    
def created_user_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
post_save.connect(created_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)

        
    

