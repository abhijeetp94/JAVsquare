from django.db import models

# Create your models here.
def get_upload_path(instance, filename):
     return 'Dairytext/{0}/{1}'.format(instance.username, filename)
def get_image_path(instance, filename):
     return 'images/{0}/{1}'.format(instance.username, filename)



class user_details(models.Model):
     
     s_n = models.AutoField
     name = models.CharField(max_length = 20)
     username = models.CharField(max_length = 16)
     password = models.CharField(max_length = 16)
     up_date = models.DateField()
     image = models.ImageField(upload_to = get_image_path, default = "")
     about = models.CharField(max_length = 1000, default = "")


     def __str__(self):
          return self.username


class note(models.Model):

     uname = models.CharField(max_length = 20)
     time = models.DateTimeField(auto_now_add = True)
     notesname = models.CharField(max_length = 50)
     notes = models.CharField(max_length = 1000)

     class Meta:
          unique_together = ('uname', 'time')

     def __str__(self):
          return self.notesname






