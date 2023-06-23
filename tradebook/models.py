from django.contrib.auth.models import User
from django.db import models
from django.template import response
# Create your models here.
class trade_post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True,blank=True)
    status = (('판매대기','판매대기'),('거래중','거래중'),('판매중','판매중'),('거래완료','거래완료'))
    status_choice = models.CharField(max_length=10,default='판매대기',choices=status)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
        return self.hit
