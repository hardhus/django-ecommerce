from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    topic = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["-timestamp"]