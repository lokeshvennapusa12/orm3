from django.db import models

class Stu(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sadd=models.CharField(max_length=200)

    def __str__(self):
        return self.sname

    
class Cour(models.Model):
    sid=models.ForeignKey(Stu,on_delete=models.CASCADE)
    cid=models.IntegerField(unique=True)
    cname=models.CharField(max_length=20)
    cduration=models.IntegerField()

    def __str__(self):
        return self.cname
