import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from main.models import Lesson
from utils.send_file import SendFile  


@receiver(post_save, sender=Lesson)
def send_lesson_files_to_telegram(instance, created, **kwargs):
    if created:
        send_file_instance = SendFile(token=os.getenv("TOKEN"))

        # Отправка аудиофайла
        if instance.audio_lesson:
            file = instance.audio_lesson.read()  # Читаем файл в оперативной памяти
            filename = instance.audio_lesson.name
            audio_file_id = async_to_sync(send_file_instance.send_file_audio)(
                chat_id=int(os.getenv("CHAT_ID")), file=file, filename=filename
            )
            instance.audiofile_id = audio_file_id

        # Сохраняем изменения
        instance.save()
