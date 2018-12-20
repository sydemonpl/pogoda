from django.db import models

class Miasto(models.Model):
    nazwa = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Miasta"
    def __str__(self):
        return self.nazwa