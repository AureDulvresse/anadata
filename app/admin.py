from django.contrib import admin

from .models import Answer, AnswerNumericData, NumericData, Question, Tag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(NumericData)
admin.site.register(AnswerNumericData)
