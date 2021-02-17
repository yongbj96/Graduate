from django.db import models

class Region(models.Model):
    region = models.IntegerField(primary_key=True)
    region_name = models.CharField(max_length=50)

    class Meta:
        db_table            = 'users_region' # 데이터베이스에 저장되는 테이블명
        verbose_name        = '지역' # 해당 테이블을 조회할 때 테이블이름
        verbose_name_plural = '지역리스트' # 해당 테이블을 조회할 때 테이블이름 (기본값 = "verbose_name"+s)

class User(models.Model):
    num = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2, null=True, default='') #M, F
    age = models.IntegerField(null=True, default=0)
    region = models.ForeignKey('Region', db_column='region', on_delete=models.CASCADE)

    class Meta:
        db_table            = 'users_user' # 데이터베이스에 저장되는 테이블명
        verbose_name        = '사용자' # 해당 테이블을 조회할 때 테이블이름
        verbose_name_plural = '사용자들' # 해당 테이블을 조회할 때 테이블이름 (기본값 = "verbose_name"+s)
