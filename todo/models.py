from django.db import models

class TodoItem(models.Model):
	text = models.TextField()
	publish_date = models.DateTimeField(auto_now_add = True)
