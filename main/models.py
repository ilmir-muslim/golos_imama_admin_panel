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


class TextStorage(S3Boto3Storage):
    location = "text_lesson"  # Папка для текстов


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
        storage=AudioStorage(),  # Используем кастомное хранилище
        blank=True,
        null=True,
        verbose_name="Аудиозапись урока",
    )
    text_lesson = models.FileField(
        storage=TextStorage(),  # Используем кастомное хранилище
        blank=True,
        null=True,
        verbose_name="Текст урока",
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


class TelegramFileId(models.Model):
    name = models.ForeignKey(
        to=Lesson, on_delete=models.CASCADE, verbose_name="Название урока"
    )
    audiofile_id = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Id аудиофайла в ТГ"
    )
    text_file_id = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Id текстового файла в ТГ"
    )

    class Meta:
        db_table = "telegram_file_id"
        verbose_name = "ИД файлов в телеграмме"
        verbose_name_plural = "ИД файлов в телеграмме"

    def __str__(self):
        return self.name.name
