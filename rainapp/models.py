from django.db import models

class ViewerData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    is_raining = models.BooleanField()  # True = Raining, False = Not Raining

    def __str__(self):
        return f"{self.name} from {self.location}"