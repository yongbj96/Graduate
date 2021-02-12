from django.db import models

class BoardMember(models.Model):
    username    = models.CharField(max_length=100, verbose_name='유저Id')
    email       = models.EmailField(max_length=100, verbose_name='유저메일')
    password    = models.CharField(max_length=100, verbose_name='유저PW')
    create_at   = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    update_at   = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')

    # 생성되는 객체의 타입을 문자열로 변환해서 보여주는 역할
    def __str__(self):
        return self.username

    # 데이터베이스에 저장되는 테이블명
    class Meta:
        db_table            = 'boardmembers'
        verbose_name        = '게시판멤버'
        verbose_name_plural = '게시판멤버'