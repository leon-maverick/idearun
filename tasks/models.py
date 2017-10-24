from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class category (models.Model):
	category_title = models.CharField(max_length=80)
	
	def __str__(self):
		return self.category_title

class task(models.Model):
	STAT = (("P","Pending"),("D","Done"))
	title=models.CharField(max_length=50)
	creation_date=models.DateTimeField(default=timezone.now)
	status=models.CharField(max_length=1, choices=STAT)
	groups = models.ForeignKey(category,on_delete=models.CASCADE)
	
	def get_absolute_url(self):
		return reverse('tasks:task-update', kwargs={'pk':self.pk})

	def __str__(self):
		return self.title
	
