<<<<<<< HEAD
from django.contrib import admin

from manageQuizz.models import *

# Register your models here.

# admin.site.register(Quizz)
# admin.site.register(Proposition)
# admin.site.register(Question)









@admin.register(Quizz)
class Quizz(admin.ModelAdmin):
    pass
@admin.register(Proposition)
class Proposition(admin.ModelAdmin):
    pass
@admin.register(Question)
class Question(admin.ModelAdmin):
    pass
=======
from django.contrib import admin

from manageQuizz.models import *

# Register your models here.

# admin.site.register(Quizz)
# admin.site.register(Proposition)
# admin.site.register(Question)









@admin.register(Quizz)
class Quizz(admin.ModelAdmin):
    pass
@admin.register(Proposition)
class Proposition(admin.ModelAdmin):
    pass
@admin.register(Question)
class Question(admin.ModelAdmin):
    pass
>>>>>>> debdd121a0ae1b44b1acc4613d7d9b75efb8eeb7
