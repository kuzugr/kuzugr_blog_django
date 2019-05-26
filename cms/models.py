from django.db import models


class Advertisements(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pc_link = models.TextField()
    sp_link = models.TextField()
    display_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'advertisements'

    def __str__(self):
        return self.name


class ArticleUploadFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    upload_file_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article_upload_files'


class Articles(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    mark_content = models.TextField()
    html_content = models.TextField()
    description = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category_id = models.IntegerField(blank=True, null=True)
    published = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'articles'

    def __str__(self):
        return self.title


class BlogInformations(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255)
    profile_name = models.CharField(max_length=255)
    profile_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_informations'

    def __str__(self):
        return self.title


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    create_user_id = models.IntegerField(blank=True, null=True)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name


class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.TextField()
    article_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'

    def __str__(self):
        return self.name


class Thumbnails(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    file_name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'thumbnails'

    def __str__(self):
        return self.file_name


class UploadFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    file_extension = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'upload_files'

    def __str__(self):
        return self.file_name


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(
        max_length=255, blank=True, null=True)
    last_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    confirmation_token = models.CharField(
        max_length=255, blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)
    unconfirmed_email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    access_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.nickname
