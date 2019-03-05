from django.db import models

# Create your models here.

class Actor(models.Model):
    """
    Class definition for actors
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Print a readable version of objects for this class
        """
        return self.name

    class Meta:
        ordering = ('name',)

class Movie(models.Model):
    """
    Class definition for movies
    """
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    year = models.IntegerField()

    def __str__(self):
        """
        Print a readable version of objects for this class
        """
        return self.title

        class Meta:
            ordering = ('title',)
