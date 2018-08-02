from django.contrib import admin
from .models import Post, Category, Project, About
from django_markdown.admin import AdminMarkdownWidget

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {'body': {'widget': AdminMarkdownWidget}}

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {'body': {'widget': AdminMarkdownWidget}}

class AboutAdmin(admin.ModelAdmin):
    formfield_overrides = {'body': {'widget': AdminMarkdownWidget}}    

admin.site.register(Post,PostAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Category)
