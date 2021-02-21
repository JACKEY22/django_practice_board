from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('account.User',on_delete=models.CASCADE, verbose_name='작성자')
    registered_at = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')

    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        ordering = ['-registered_at']
        verbose_name = '게시글'
        verbose_name_plural = '게시글'


