from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models.TaskQuestionAudio import TaskQuestionAudio
from app.models.TaskQuestionMCQ import TaskQuestionMCQ
from app.models.TaskQuestionVideo import TaskQuestionVideo
from app.models.CourseTaken import CourseTaken 
from app.models.CourseTask import CourseTask
from app.models.Modul import Modul
from app.models.Quest import Quest

@receiver(post_save, sender=TaskQuestionAudio)
def create_task_question(sender, instance, created, **kwargs):
    if created:
        TaskQuestionMCQ.objects.create(
            modul=instance.modul,
            question_text=instance.answer,
            option1=instance.question_text,
            option2='',  # Fill as needed
            option3='',  # Fill as needed
            option4=''   # Fill as needed
        )
        TaskQuestionVideo.objects.create(
            modul=instance.modul,
            question_text=instance.answer,
            video=None,  # You can set a default value or handle it as needed
            option1=instance.question_text,
            option2='',  # Fill as needed
            option3='',  # Fill as needed
            option4=''   # Fill as needed
        )

@receiver(post_save, sender=CourseTaken)
def create_quests_for_course(sender, instance, created, **kwargs):
    if created:
        tasks = CourseTask.objects.filter(course=instance.course)
        for task in tasks:
            modules = Modul.objects.filter(course_task=task)
            for modul in modules:
                Quest.objects.create(
                    user=instance.user,
                    course_taken=instance,
                    course_task=task,
                    modul=modul
                )