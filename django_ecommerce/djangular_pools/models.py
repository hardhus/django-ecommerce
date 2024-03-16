from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now=True)

    def pool_items(self):
        return self.poolitem_set.all()

class PoolItem(models.Model):
    poll = models.ForeignKey(Poll, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    class Meta:
        ordering = ["-text"]