from django.db import models

# Create your models here.
class BDE_User(models.Model):
    emp_code = models.IntegerField()
    emp_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256,unique=True)
    password = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.emp_name
    
class Project(models.Model):
    project_name = models.CharField(max_length=256)
    date = models.DateField(default='',blank=True)
    technology = models.CharField(max_length=256, blank=True)
    resume_shared = models.BooleanField(default=False)
    edited_by = models.ForeignKey(BDE_User,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return self.project_name

            
            
class Round1(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(default='',blank=True,null=True)
    screenshot_shared = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    our_review = models.TextField(default='',blank=True)   
    client_review = models.TextField(default='')
    edited_by = models.ForeignKey(BDE_User,on_delete=models.SET_NULL,null=True) 
    def __str__(self) -> str:
        return f"{self.project}"    

class Round2(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(default='',blank=True,null=True)
    screenshot_shared = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    our_review = models.TextField(default='',blank=True)   
    client_review = models.TextField(default='',blank=True)
    edited_by = models.ForeignKey(BDE_User,on_delete=models.SET_NULL,null=True)   
    def __str__(self) -> str:
        return f"{self.project}"

class Round3(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(default='',blank=True,null=True)
    screenshot_shared = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    our_review = models.TextField(default='',blank=True)   
    client_review = models.TextField(default='',blank=True)
    edited_by = models.ForeignKey(BDE_User,on_delete=models.SET_NULL,null=True)   
    def __str__(self) -> str:
        return f"{self.project}"