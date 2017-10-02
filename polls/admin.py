from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
    Tells Django that Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.
    """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """
    Choose order so pub_date comes before question_text.
    Split form up into fieldsets.
    First element in each tuple in fieldsets is the title of the fieldset.
    """
    fieldsets = [
        (None,             {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


    # fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

