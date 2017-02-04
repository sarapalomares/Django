from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validateReg(self,request):
        error = self.validateRegInputs(request)
        print error

        if len(error) > 0:
            return (False,error)

        pw_hash=bcrypt.hashpw(request.POST['pw_create'].encode(), bcrypt.gensalt())

        user = self.create(name=request.POST['name'], alias=request.POST['alias'], pw_hash=pw_hash)

        return(True, user)

    def validateRegInputs(self,request):
        error=[]
        if not request.POST['name'].isalpha():
            error.append("Your name cannot have numbers.")
        if len(request.POST['name']) < 2:
            error.append("Please input a valid name.")
        if not EMAIL_REGEX.match(request.POST['reg_email']):
            error.append("Please input a valid email address.")
        if len(request.POST['pw_create']) < 8 or request.POST['pw_create'] != request.POST['pw_confirm']:
            error.append("Passwords do not match. Try again.")
        return error

    def validateLogin(self,request):
        try:
            user = User.objects.get(email=request.POST['user_email'])
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode():
                return (True, user)

        except ObjectDoesNotExist:
            return(False, ["Email & Password do not match. Try again."])

class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    pw_hash = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
