from django.db import models
from django.utils import timezone

class OddsList(models.Model):
   event_date = models.DateTimeField            #日付
   place      = models.CharField(max_length=30) #競馬場名
   corse_type = models.CharField(max_length=30, null=True) #コース距離
   race_no    = models.IntegerField() #レース番号
   horse_no   = models.IntegerField() #馬番
   win_odds   = models.DecimalField(max_digits=4,decimal_places=1) #単勝オッズ
   show_odds1 = models.DecimalField(max_digits=4,decimal_places=1) #複勝オッズ
   show_odds2 = models.DecimalField(max_digits=4,decimal_places=1) #複勝オッズ２

class Keibajou(models.Model):
   place  = models.CharField(max_length=20) #競馬場名
   course = models.CharField(max_length=30) #コース距離

class KeibaReporter(models.Model):
   name     = models.CharField(max_length=30) #氏名
   attached = models.CharField(max_length=10) #所属
   status   = models.CharField(max_length=10) #状態
   Hitting  = models.FloatField()             #的中率

class Jockey(models.Model):
   name       = models.CharField(max_length=30)#氏名
   attached   = models.CharField(max_length=10)#所属
   birthday   = models.DateField()#誕生日
   total_wins = models.IntegerField()#総合勝利数
   status     = models.CharField(max_length=10)#状態

class JsonData(models.Model):
   json_data = models.FileField(upload_to='model_data')

class TestHoldingInfo(models.Model):
   date      = models.DateField()#開催日
   place     = models.CharField(max_length=20)
   race_name = models.CharField(max_length=30)

