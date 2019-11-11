from django.db import models

# Create your models here.

class Country(models.Model):

    name = models.TextField()

    def __str__(self): return self.name


class Song(models.Model):

    CHOICES = (
        ('r' , 'Rock'),
        ('p' , 'Pop'),
        ('j', 'Jazz'),
        ('h', 'Hip Hop'),
        ('m', 'Metal')
    )

    title = models.TextField()
    genre = models.CharField(max_length=1,choices=CHOICES)
    release_date = models.DateField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    singers = models.ManyToManyField('Person')

    def __str__(self):
        return self.title 

class Person(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.IntegerField()

    def __str__(self): 
        return self.first_name + " " + self.last_name

    

