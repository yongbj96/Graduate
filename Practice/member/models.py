from django.db import models

class BoardMember(models.Model):
    username    = models.CharField(max_length=100, verbose_name='유저Id')
    password    = models.CharField(max_length=100, verbose_name='유저PW')
    email       = models.EmailField(max_length=100, verbose_name='유저메일')
    create_at   = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    update_at   = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')

    # 생성되는 객체의 타입을 문자열로 변환해서 보여주는 역할
    def __str__(self):
        return self.username

    class Meta:
        db_table            = 'boardmembers' # 데이터베이스에 저장되는 테이블명
        verbose_name        = '게시판멤버' # 해당 테이블을 조회할 때 테이블이름
        verbose_name_plural = '게시판멤버들' # 해당 테이블을 조회할 때 테이블이름 (기본값 = "verbose_name"+s)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table            = 'board'
        verbose_name        = '게시판'
        verbose_name_plural = '게시판목록'