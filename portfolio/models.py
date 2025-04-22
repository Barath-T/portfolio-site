from django.db import models
from django.shortcuts import reverse




DIV_CHOICES = [
	('1st', 'aboutWhat'),
	('2nd', 'whatsInThere'),
	('3rd', 'concluding')	,						
]

class Project(models.Model):
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=500)
	small_desc = models.TextField()
	pic = models.ImageField(default='default.jpg')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("project-detail", kwargs={'pk': self.pk})


class Describe(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='desc_name') #Project.objects.filter(description='1')  
	desc_name = models.CharField(max_length=255, choices=DIV_CHOICES,)
	title = models.CharField(max_length=500)
	description = models.TextField()

	def __str__(self):
		return self.desc_name


class Image(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='img_name') 
	img_name = models.CharField(max_length=255, choices=DIV_CHOICES,)
	images = models.ImageField()

	def _str__(self):
		return self.img_name


class Skill(models.Model):
	skill_name = models.CharField(max_length=255)
	skill_desc = models.TextField()
	skill_img = models.ImageField()

	def __str__(self):
		return self.skill_name


