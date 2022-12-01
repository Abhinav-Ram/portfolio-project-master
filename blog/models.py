from django.db import models

#create model
class  Blog(models.Model):
	title  = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()
	body = models.TextField( )
	image = models.ImageField(upload_to='images/')
	link = models.URLField(max_length=200,default="",blank=True)
	def __str__(self):
		return self.title
	def summary(self):
		return self.body[:100] + '...'
	def format_date(self):
		return self.pub_date.strftime('%B %e, %Y (%A)')
	

#add blog app to settings

#create migration

#migrate

#add to admin
