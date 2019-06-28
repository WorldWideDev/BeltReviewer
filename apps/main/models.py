from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    # reviews_written 

class Book(models.Model):
    title = models.CharField(max_length=45)

    # reviews_recieved 

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    books = models.ManyToManyField(Book, related_name="authors")
    
class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField()

    reviewer = models.ForeignKey(User, related_name="reviews_written")
    # reviewer_id 
    book = models.ForeignKey(Book, related_name="reviews_recieved")
    # book_id
