from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
	def validator(self, postData):
		errors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(postData['first_name']) < 2:
			errors['first_name'] = "Your first name must be more than 2 characters"
		if len(postData['last_name']) < 2:
			errors['lasst_name'] = "Your last name must be more than 2 characters"
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Email must be valid format"
		if len(postData['password']) < 8:
			errors['password'] = "Password must be at least 8 characters"
		if postData['password'] != postData['confirm_password']:
			errors['confirm_password'] = "Password and Confirm Password do not match"
		return errors


	def review_validation(self, postData):
		errors = {}
		if len(postData['new_review']) < 10:
			errors['new_quote'] = 'Review field should be at least 10 characters...!!!'
		return errors


class User (models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Reviews (models.Model):
	review = models.CharField(max_length=255)
	creator = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)