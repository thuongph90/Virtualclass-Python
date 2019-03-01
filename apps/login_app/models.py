from django.db import models
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['user_name'])<2:
            errors['user_name']="user_name should be at least 2 chars."
        elif 'catergory' not in postData:
            errors['catergory']="Please choose who you are."
        elif len(postData['email'])<5:
            errors['email']="email is invalid."
        elif len(postData['password'])<8:
            errors['first_name']="password should be at least 8 chars."
        elif len(postData['phone_number'])<9:
            errors['phone_number']="Phone number is invalid"
        elif postData['password']!=postData['repassword']:
            errors['first_name']="password should match"
        return errors
    def account_validator(self,postData):
        errors={}
        if len(postData['user_name'])<2:
            errors['user_name']="user_name should be at least 2 chars."
        elif len(postData['email'])<5:
            errors['email']="email is invalid."
        elif len(postData['phone_number'])<9:
            errors['phone_number']="Phone number is invalid"
        return errors
    def post_validator(self,postData):
        errors={}
        if len(postData['post'])<2:
            errors['post']="A post should be at least 2 chars."
        return errors


class register(models.Model):
    user_name=models.CharField(max_length=50)
    email=models.CharField(max_length=250)
    phone_number=models.IntegerField()
    password=models.CharField(max_length=25)
    catergory=models.CharField(max_length=25)
    score=models.IntegerField(default=0)
    objects=UserManager()

class Posts(models.Model):
    teacher=models.ForeignKey(register, related_name="teacher")
    main_post=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Comments(models.Model):
    post=models.ForeignKey(Posts, related_name="comments")
    comment=models.TextField()
    result=models.TextField(max_length=250, default = None, null=True)
    students=models.ForeignKey(register, related_name="student")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    likes=models.ManyToManyField(register, related_name="likes")

class Notes(models.Model):
    teacher= models.ForeignKey(register, related_name="from_note")
    student= models.ForeignKey(register, related_name="to_note")
    notes= models.TextField(max_length=250, default = None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()