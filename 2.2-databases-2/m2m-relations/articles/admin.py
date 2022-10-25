from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, Teg


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            cl_data = form.cleaned_data
            if cl_data != {}:
                if cl_data['is_main']:
                    count += 1
        if count > 1:
            raise ValidationError('Значение  is_main > 1')
        elif count == 0:
            raise ValidationError('Значение  is_main = 0')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Teg)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']
    list_filter = ['title']
    inlines = [ScopeInline, ]
