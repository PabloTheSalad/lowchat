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

