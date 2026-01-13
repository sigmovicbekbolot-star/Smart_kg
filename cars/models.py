from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='phone/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"