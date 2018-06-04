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