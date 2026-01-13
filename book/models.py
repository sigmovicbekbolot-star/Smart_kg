from django.db import models




class Book(models.Model):
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    year = models.IntegerField()
    cover = models.ImageField(upload_to='cover/')
    is_available = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
