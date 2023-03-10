from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    questionContent = models.CharField(max_length=200,unique=True)
    answer = models.CharField(max_length=50)

class Rules(models.Model):
    hash_value = models.CharField(max_length=50,default="")
    sid = models.CharField(max_length=10)
    rev = models.CharField(max_length=10)
    rule = models.CharField(max_length=9000,default="")
    file_name = models.CharField(max_length=20,default="")
    update_time = models.CharField(max_length=20,default="")
    state = models.CharField(max_length=5,default="")

# 创建英雄类(多类)
class HeroInfo(models.Model):

    # 英雄名
    hname = models.CharField(max_length=20)

    # 英雄性别
    hgender = models.BooleanField(default=False)

    # 英雄功法
    hkunfu = models.CharField(max_length=80)


# 创建书的类(1类)
class BookInfo(models.Model):

    # 书名
    bname = models.CharField(max_length=20)

    # 书的日期
    bpud_date = models.DateField()

    # def __str__(self):
    #
    #     return self.bname

