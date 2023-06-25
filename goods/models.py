from django.db import models




class Goods(models.Model):
      bname=models.CharField(max_length=100)        # 책 제목\
      image= models.ImageField(upload_to='goodds/%Y/%m/%d',
                               blank=True)                                  # 책사진
      price = models.DecimalField(max_digits=10,decimal_places=2) #10자리숫자까지 만듨 있음 / 소수리 2까지  총 8자리 금액임
                                                                  # 금액 990,000
      #url=models.URLField('Site URL',default = '')

      # class Meta:
      #     ordering = ['-created']

      # def __str__(self):
      #       return self.name


def __str__(self):
      return self.bname
