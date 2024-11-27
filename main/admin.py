from django.contrib import admin

from main.models import Themes, Lesson, Chapter


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Themes)
class ThemesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
