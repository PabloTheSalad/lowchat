from django.db import models

from django.contrib.auth.models import User

"""
class Chat(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
"""


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.user.username + ' [' + str(self.pub_date.ctime()) + ']: ' + self.text[:32])

    class Meta:
        ordering = ('pub_date',)

    def gettime(self):
        time = self.pub_date.time()
        hour = time.hour
        minute = time.minute
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
        if minute < 10:
            minute = '0' + str(minute)
        else:
            minute = str(minute)

        return hour + ':' + minute


class Features(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='staticfiles/chat/p_images/', max_length=100, default='chat/static/chat/p_images/default.jpg')
    age = models.DateField()
    gender = models.CharField(max_length=1)
    information = models.CharField(max_length=1024)
    namecolor = models.CharField(max_length=32, default='black')
    last_enter = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.user.username + ' features')

    def getimg(self):
        return '/static/' + '/'.join(self.image.url.split('/')[1:])
