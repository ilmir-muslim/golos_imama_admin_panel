from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class Chapter(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название раздела"
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "chapter"
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.name


class Themes(models.Model):
    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название темы урока"
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    chapter = models.ForeignKey(
        to=Chapter, on_delete=models.CASCADE, verbose_name="Раздел"
    )

    class Meta:
        db_table = "theme"
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.name

# Специальные хранилища для разделения файлов по папкам
class AudioStorage(S3Boto3Storage):
    location = "audio_lesson"  # Папка для аудиофайлов



class Lesson(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название урока")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    annotation = models.TextField(blank=True, null=True, verbose_name="Описание урока")
    video_lesson = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Видео урока"
    )
    audio_lesson = models.FileField(
        storage=AudioStorage(),
        blank=True,
        null=True,
        verbose_name="Аудиозапись урока",
    )
    audiofile_id = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Id аудиофайла в ТГ"
    )
    theme = models.ForeignKey(
        to="Themes", on_delete=models.CASCADE, verbose_name="Тема"
    )

    class Meta:
        db_table = "lesson"
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name

    