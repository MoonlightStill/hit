from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.IntegerField(max_length = 15, primary_key = True)
    Name = models.CharField(max_length = 20)
    Age = models.IntegerField(max_length = 3)
    Country = models.CharField(max_length = 15)
    class Meta:
        db_table = 'Author'
        

class Book(models.Model):
    ISBN = models.IntegerField(max_length = 13,primary_key = True)
    Title = models.CharField(max_length = 35)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 35)
    PublishDate = models.DateField()
    Price = models.CharField(max_length = 15)
    class Meta:
        db_table = 'Book'
        
    