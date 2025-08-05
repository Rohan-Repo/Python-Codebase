from django.db import models

class Movie(models.Model):
    # As title is a String Value
    title = models.CharField( max_length=100 )
    # As Year is an Integer value
    year = models.IntegerField(default=0)

    # We do this so in our Django admin we see proper names
    def __str__(self):
        return f'{self.title} from the year : {self.year}'