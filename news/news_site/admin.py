import re
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Category, News
# Register your models here.


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'create_up', 'category', 'is_pablished', 'views', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_pablished',)
    list_filter = ('is_pablished', 'category')
    fields = ('title', 'content', 'photo', 'get_photo', 'is_pablished', 'views', 'create_up', 'updated_up')
    readonly_fields = ('get_photo', 'views', 'create_up', 'updated_up')
    # save_on_top = True

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="75">')
        else: 
            return 'Фото не установлено'
    
    get_photo.short_description = 'Миниатюра'


class CategotyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategotyAdmin)
admin.site.site_title = 'Панель администратора'
admin.site.site_header = 'Панель администратора'