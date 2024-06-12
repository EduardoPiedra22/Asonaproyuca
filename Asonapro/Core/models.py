from django.db import models
from django.conf import settings


class BaseModel(models.Model):
	user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_creation', null=True, blank=True)
	date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_update', null=True, blank=True)
	date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
	

	def toJSON(self):
		item = model_to_dict(self)
		item['user_creation'] = self.user_creation.toJSON()
		return item

	def __str__(self):
		return '{}'.format(self.user_creation.first_name)

	class Meta:
		abstract = True
		