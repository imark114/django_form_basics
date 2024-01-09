from django.db import models

# Create your models here.
class myModel(models.Model):
    id_num = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    name = models.CharField(max_length=200)
    date = models.DateField()
    date_time = models.DateTimeField()
    email = models.EmailField()
    # file_field = models.FileField(upload_to='/files')
    text = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return f"Name: {self.name} ID {self.id_num}"
    