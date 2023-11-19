from django.db import models
from django.urls import reverse


class Conf_hall(models.Model):

	hall_name = models.CharField(max_length=30, db_index=True, default="")
	venue = models.CharField(max_length=30, db_index=True, default="")
	city = models.CharField(max_length=30, db_index=True, default="")
	hall_people_capacity = models.CharField(max_length=30, db_index=True, default="")
	building_location = models.CharField(max_length=30, db_index=True, default="")
	building_standard = models.CharField(max_length=30, db_index=True, default="")
	interior_styling_standard = models.CharField(max_length=30, db_index=True, default="")
	video_conferencing_facilities_standard = models.CharField(max_length=30, db_index=True, default="")
	broadband_speed = models.DecimalField(max_digits=20, decimal_places=0, default=0)
	international_airport_proximity = models.DecimalField(max_digits=20, decimal_places=0, default=0)
	minimum_lease_period = models.DecimalField(max_digits=20, decimal_places=0, default=0)
	day_price = models.DecimalField(max_digits=20, decimal_places=0, default=0)


	class Meta:
	
		ordering = ('hall_name',)
		verbose_name = 'conf_hall'
		verbose_name_plural = 'conf_halls'
	
	def __str__(self):
	
		return self.hall_name
	
	def get_absolute_url(self):
	
		return reverse('validator:conf_hall_detail', args=[self.id])





















































