from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app.models.Course import Course
from app.models.CourseTaken import CourseTaken
from app.models.CourseTask import CourseTask
from app.models.TaskQuestionFill import TaskQuestionFill
from app.models.TaskQuestionVideo import TaskQuestionVideo
from app.models.TaskQuestionAudio import TaskQuestionAudio
from app.models.TaskQuestionMCQ import TaskQuestionMCQ
from app.models.CourseTakenProgress import CourseTakenProgress
from app.models.Quest import Quest
from app.models.FAQ import FAQ
from app.models.Question import Question
from app.models.Profile import Profile
from app.models.Profile import Language


#from app.models.UserDetails import UserDetails
from app.models.Modul import Modul
from django.contrib.sessions.models import Session

# Register each model with the admin site
admin.site.register(Course)
admin.site.register(CourseTaken)
admin.site.register(CourseTask)
admin.site.register(TaskQuestionFill)
admin.site.register(TaskQuestionVideo)
admin.site.register(TaskQuestionAudio)
admin.site.register(TaskQuestionMCQ)
admin.site.register(CourseTakenProgress)
admin.site.register(Quest)
admin.site.register(FAQ)
admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Language)
#admin.site.register(UserDetails)
admin.site.register(Modul)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'level', 'progress', 'status')
    list_filter = ('level', 'progress')
    search_fields = ('title',)

    # Jika Anda ingin mengurutkan berdasarkan 'status', Anda bisa menambahkan metode berikut:
    def status(self, obj):
        return obj.status
    
    status.admin_order_field = 'progress'  # Memungkinkan pengurutan berdasarkan 'progress'

class CoursessAdmin(admin.ModelAdmin):
    list_display = ('name', 'vers', 'progress', 'total_task')  # customize the list display
    search_fields = ('name', 'vers')  # add search fields
    list_filter = ('vers',)  # add filter by version

class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'expire_date', 'get_decoded_session_data']

    def get_decoded_session_data(self, obj):
        return obj.get_decoded()
    get_decoded_session_data.short_description = 'Session Data'

admin.site.register(Session, SessionAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'query')
    search_fields = ('name', 'email')

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('username', 'email')