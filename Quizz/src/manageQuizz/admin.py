from django.contrib import admin

from manageQuizz.models import *

# Register your models here.

# admin.site.register(Quizz)
# admin.site.register(Proposition)
# admin.site.register(Question)









@admin.register(Quizz)
class Quizz0():
    pass
@admin.register(Proposition)
@admin.register(Question)
