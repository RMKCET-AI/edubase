from django.contrib import admin
from .models import AI_Subject, ai_note, CSE_Subject, cse_note, IT_Subject, it_note, BlogPost
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.utils import get_attachment_model


# Register your models here.
class ChoiceInlineAI(admin.TabularInline):
    model = ai_note
    extra = 1


class AI_contentAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlineAI]


admin.site.register(AI_Subject, AI_contentAdmin)


class ChoiceInlineCSE(admin.TabularInline):
    model = cse_note
    extra = 1


class CSE_contentAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlineCSE]


admin.site.register(CSE_Subject, CSE_contentAdmin)


class ChoiceInlineIT(admin.TabularInline):
    model = it_note
    extra = 1


class IT_contentAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlineIT]


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(IT_Subject, IT_contentAdmin)
admin.site.register(BlogPost, PostAdmin)
# admin.site.unregister(get_attachment_model())