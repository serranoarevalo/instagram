from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_model

@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator=models.ForeignKey(user_model.User, null=True, related_name='images') 
    

    def __str__(self):
        return'{} - {}'.format(self.location,self.caption)

    class Meta:
        ordering = ['-created_at']

@python_2_unicode_compatible

class Comment(TimeStampedModel):
    '''Comment Model'''

    message=models.TextField()
    creator = models.ForeignKey(user_model.User, null=True)
    image=models.ForeignKey(Image, null=True, related_name='comments')

    def __str__(self):
        return self.message

@python_2_unicode_compatible
class Like(TimeStampedModel):
    '''Like Model'''

    creator= models.ForeignKey(user_model.User,  null=True)
    image =models.ForeignKey(Image,  null=True, related_name='likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)
