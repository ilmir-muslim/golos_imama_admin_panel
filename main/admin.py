from django.contrib import admin

from main.models import Themes, Lesson, Сhapter


@admin.register(Сhapter)
class СhapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Themes)
class ThemesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    # Функция сгенерирована ИИ и вызывает сомнения, нужно перепроверить
    # def save_model(self, request, obj):
    #     file = request.FILES['audiofile_id']
    #     bot = Bot(token='YOUR_TELEGRAM_TOKEN')
    #     bot.send_document(chat_id='YOUR_CHAT_ID', document=file)
    #     file_id = bot.get_file(file_id=bot.get_file_id(file)).file_id
    #     obj.audiofile_id = file_id
    #     obj.save()
