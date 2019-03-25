# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models


class Picture(models.Model):
    
    name = models.CharField(max_length =30)
    # picture_Main_pic = models.PictureField(upload_to='instagram/') 
    like = models.IntegerField(default=0)
    # profile = models.ForeignKey(Profile, null=True, blank=True)

    def __str__(self):
        return self.name

    def save_picture(self):
        self.save()
    
   
    def display_picture(self):
        self.display()

    def delete_picture(self):
        self.delete()
    
    
    @classmethod
    def get_picture(cls,id):
        return Picture.objects.get(id=id)

    class Meta:
        ordering = ['name']
    
     

class Profile(models.Model):
    name = models.CharField(max_length =30)
    # picture_Main_pic = models.PictureField(upload_to='instagram/') 
    bio = models.CharField(max_length =300)
    # user = models.ForeignKey(Location, null=True, blank=True)

    def __str__(self):
        return self.name


    def save_picture(self):
        self.save()

    def delete_picture(self):
        self.delete()

    def update_picture(self):
        self.update()
    
    def display_picture(self):
        self.display()

    
class Follow(models.Model):
    
    follower = models.IntegerField(default =30)
    following = models.IntegerField(default =30)
    profile = models.ForeignKey(Profile, null=True, blank=True)

    def __str__(self):
        return self.follower 

    def save_follower(self):
        self.save()

    def delete_follower(self):
        self.delete()

class Like(models.Model):
    
    profile = models.ForeignKey(Profile, null=True, blank=True)
    
    def __str__(self):
        return self.profile 

    def save_like(self):
        self.save()

    def delete_like(self):
        self.delete()

class Comment(models.Model):
    
    comments = models.CharField(max_length =30)
    picture = models.ForeignKey(Picture, null=True, blank=True)
    # user = models.ForeignKey(Picture, null=True, blank=True)
    
    def __str__(self):
        return self.comments

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


class SignUpRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
