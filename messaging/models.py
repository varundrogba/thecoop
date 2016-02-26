from django.db import models


class Messages(models.Model):
    message = models.CharField(max_length=500)
    m_dtime = models.DateTimeField(auto_now=True, auto_now_add=True)
    message_origin= models.CharField(max_length=30)
