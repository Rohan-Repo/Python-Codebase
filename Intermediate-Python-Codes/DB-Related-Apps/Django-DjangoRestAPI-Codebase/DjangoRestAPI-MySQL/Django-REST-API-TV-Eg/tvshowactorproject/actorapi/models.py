from django.db import models

# Create your models here.
class TVShowActorsModel(models.Model):
    showName = models.CharField(max_length=50)
    actorShowName = models.CharField(max_length=50)
    actorRealName = models.CharField(max_length=50)

    def __str__(self):
        return F"{self.actorRealName} played {self.actorShowName} on {self.showName}"