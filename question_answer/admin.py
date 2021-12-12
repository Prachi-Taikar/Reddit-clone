from django.contrib import admin
from . models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display=['question', 'category', 'status', 'added_date']
    list_filter=('status', 'added_date')


class AnswerAdmin(admin.ModelAdmin):
    list_display=['question', 'answer', 'added_date', 'up_voting', 'down_voting']

admin.site.register(Answer, AnswerAdmin) 
admin.site.register(Question, QuestionAdmin) 