from django.db import models

from django.shortcuts import reverse

CATEGORY_CHOICES = (
	('S', 'Shirt'), 
	('TS', 'T-Shirt'), 
	('P', 'Polo')
	)

LABEL_CHOICES=(
	('P', 'primary'),
	('S', 'secondary'),
	('D', 'danger'),
	)

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse("product-detail", kwargs={'pk': self.pk})
