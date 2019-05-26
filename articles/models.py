from django.db import models


class Article(models.Model):
    title = models.CharField('記事名', max_length=255)
    mark_content = models.TextField('マークダウン本文')
    html_content = models.TextField('HTML本文')
    description = models.CharField('SEO用概要', max_length=255)
    user_id = models.IntegerField('User ID')
    created_at = models.DateTimeField('作成日', blank=False)
    updated_at = models.DateTimeField('更新日', blank=False)
    category_id = models.IntegerField('カテゴリーID', blank=True)
    published = models.BooleanField('公開フラグ')

    class Meta:
        db_table = 'articles'

    def __str__(self):
        return self.title
