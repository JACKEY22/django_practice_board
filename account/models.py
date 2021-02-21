from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='계정명')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일자')

    def __str__(self): # 객체 문자열 반환 내장함수
        return self.username

    class Meta: # 데이터베이스 관련 정보
        db_table = 'user' # 테이블 이름
        ordering = ['-registered_at']
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
