from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    form=PostAdminForm
    save_as = True
    readonly_fields = ('views','created_at','get_photo',)
    search_fields = ('title',)
    list_filter = ('category','tags',)
    list_display_links = ('title',)
    list_display = ('id','title','slug','category','created_at','get_photo')
    fields = ('title','slug','category','tags','content','photo',
              'created_at','get_photo','views','posted_by')

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}"width=50>')
        return '--'

    get_photo.short_description='Фото'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)
