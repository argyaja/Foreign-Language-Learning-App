    # from app.views.Noa import about, accordion, alerts, avatar, background, badge, blog, blog_details, blog_edit, border, breadcrumbs
from . import views
from app.views.Noa import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views.Login import login
from app.views.Logout import logout
from app.views.Register import registerPage
from app.views.Home import home
from app.views.Courses import courses
from app.views.Course_take import take_course
from app.views.Course_Task import course_tasks,course_task_list_add, course_task_create, course_task_update, course_task_delete
from app.views.Modul_detail import Modul_detail
from app.views.FAQ import faq_view
from app.views.Quest import quest
from app.views.Modul_Detail_Admin import modul_create, modul_edit, modul_update, modul_delete
from app.views.Leaderboards import leaderboards
from app.views.Quiz import quiz
from app.views.Lesson_complite import lesson_complite
from app.views.AdminCourses import admin_courses, admin_add_course, admin_delete_course, admin_edit_course, admin_update_course
from app.views.Preview import preview
from app.views.ProfileView import profile_view
from app.views.ProfileView import edit_profile
from app.views.PasswordView import confirm_password,change_password

app_name = 'app'
urlpatterns = [
    # path('user_info/', views.user_info, name='user_info'),
    ## Default Homepage (Login)
    path('', login, name='login'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    
    ## Register
    # path('register1', registerPage, name='register1'),
    path('register', registerPage, name='registerOG'),

    ## Home (Show courses for user)
    path('home', home, name='home'),
    path('leaderboards', leaderboards, name='leaderboards'),

    # Courses (show courses for user)
    path('courses', courses, name='courses'),
    path('take_course/<int:id>/', take_course, name='take_course'),
    
    # Courses (Show courses for admin)
    path('administrator/courses', admin_courses, name='admin-courses'),
    path('administrator/course/create/', admin_add_course, name='admin-add-course'),  
    path('administrator/course/edit/<int:id>', admin_edit_course, name='admin-edit-course'),  
    path('administrator/course/update/<int:id>', admin_update_course, name='admin-update-course'),  
    path('administrator/course/delete/<int:id>', admin_delete_course, name='admin-delete-course'),

    ## Course Tasks
    path('course/tasks/<int:course_id>', course_tasks, name='course_tasks'),
    path('course/task/create/<int:course_id>/', course_task_create, name='course_task_create'),
    path('tasks/update/<int:pk>/', course_task_update, name='course_task_update'),
    path('course/task/delete/<int:pk>/', course_task_delete, name='course_task_delete'),


    ## Quiz
    path('course/<int:course_id>/task/<int:task_id>/quiz/', quiz, name='quiz'),
    path('preview', preview, name='preview'),
    # path('course/<int:course_id>/task/<int:task_id>/quiz/<int:taskquestion_id>/', quiz, name='quiz'),
    # other URL patterns
    path('quiz_mcq', quiz_mcq, name='quiz_mcq'),
    ## FAQ
    path('faq/', faq_view, name='faq'),

    ## Quest
    path('quest', quest, name='quest'),

    ##Modul Detail
    path('course/<int:course_id>/task/<int:task_id>/', Modul_detail, name='Modul_detail'),
    path('course/<int:course_id>/task/<int:task_id>/modul/create/', modul_create, name='modul_create'),
    path('course/<int:course_id>/task/<int:task_id>/modul/edit/<int:modul_id>/', modul_edit, name='modul_edit'),
    path('course/<int:course_id>/task/<int:task_id>/modul/update/<int:modul_id>/', modul_update, name='modul_update'),
    path('course/<int:course_id>/task/<int:task_id>/modul/delete/<int:modul_id>/', modul_delete, name='modul_delete'),


    ## Lesson Complite
     path('lesson_complite', lesson_complite, name='lesson_complite'),

    # Profile
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    #path('profileFake', profile_view, name='profileFake'),

    # Password Change
    path('confirm-password/', confirm_password, name='confirm_password'),
    path('change-password/', change_password, name='change_password'),
    

    ## Bawaan
    path('', login, name='login'),
    path('about', about, name='about'),
    path('accordion', accordion, name='accordion'),
    path('alerts', alerts, name='alerts'),
    path('avatar', avatar, name='avatar'),
    path('background', background, name='background'),
    path('badge', badge, name='badge'),
    path('blog-details', blog_details, name='blog-details'),
    path('blog-edit', blog_edit, name='blog-edit'),
    path('blog', blog, name='blog'),
    path('border', border, name='border'),
    path('breadcrumbs', breadcrumbs, name='breadcrumbs'),
    path('buttons', buttons, name='buttons'),
    path('calendar2', calendar2, name='calendar2'),
    path('form-elements', form_elements, name='form-elements'),
    path('form-layouts', form_layouts, name='form-layouts'),
    path('form-validation', form_validation, name='form-validation'),
    path('form-wizard', form_wizard, name='form-wizard'),
    path('gallery', gallery, name='gallery'),
    path('height', height, name='height'),
    path('icons', icons, name='icons'),
    path('icons2', icons2, name='icons2'),
    path('icons3', icons3, name='icons3'),
    path('icons4', icons4, name='icons4'),
    path('icons5', icons5, name='icons5'),
    path('icons6', icons6, name='icons6'),
    path('icons7', icons7, name='icons7'),
    path('icons8', icons8, name='icons8'),
    path('icons9', icons9, name='icons9'),
    path('icons10', icons10, name='icons10'),
    path('index', index, name='index'),
    path('invoice-create', invoice_create, name='invoice-create'),
    path('invoice-details', invoice_details, name='invoice-details'),
    path('invoice-edit', invoice_edit, name='invoice-edit'),
    path('invoice-list', invoice_list, name='invoice-list'),
    path('invoice-timelog', invoice_timelog, name='invoice-timelog'),
    path('landing', landing, name='landing'),
    path('loaders', loaders, name='loaders'),
    path('lockscreen', lockscreen, name='lockscreen'),
    path('mail-compose', mail_compose, name='mail-compose'),
    path('mail-inbox', mail_inbox, name='mail-inbox'),
    path('mail-read', mail_read, name='mail-read'),
    path('mail-settings', mail_settings, name='mail-settings'),
    path('maps', maps, name='maps'),
    path('maps1', maps1, name='maps1'),
    path('maps2', maps2, name='maps2'),
    path('margin', margin, name='margin'),
    path('mediaobject', mediaobject, name='mediaobject'),
    path('modal', modal, name='modal'),
    path('navigation', navigation, name='navigation'),
    path('notify', notify, name='notify'),
    path('offcanvas', offcanvas, name='offcanvas'),
    path('opacity', opacity, name='opacity'),
    path('padding', padding, name='padding'),
    path('pagination', pagination, name='pagination'),
    path('panels', panels, name='panels'),
    path('position', position, name='position'),
    path('pricing', pricing, name='pricing'),
    path('product-details', product_details, name='product-details'),
    path('products', products, name='products'),
    
    path('progress', progress, name='progress'),
    path('project-details', project_details, name='project-details'),
    path('project-edit', project_edit, name='project-edit'),
    path('project-new', project_new, name='project-new'),
    path('projects-list', projects_list, name='projects-list'),
    path('projects', projects, name='projects'),
    path('rangeslider', rangeslider, name='rangeslider'),
    path('rating', rating, name='rating'),
    path('scroll', scroll, name='scroll'),
    path('services', services, name='services'),
    # path('settings', settings, name='settings'),
    path('sweetalert', sweetalert, name='sweetalert'),
    path('switcherpage', switcherpage, name='switcherpage'),
    path('table-editable', table_editable, name='table-editable'),
    path('tables', tables, name='tables'),
    path('tabs', tabs, name='tabs'),
    path('tags', tags, name='tags'),
    path('task-create', task_create, name='task-create'),
    path('task-edit', task_edit, name='task-edit'),
    path('tasks-list', tasks_list, name='tasks-list'),
    path('terms', terms, name='terms'),
    path('thumbnails', thumbnails, name='thumbnails'),
    path('ticket-details', ticket_details, name='ticket-details'),
    path('timeline', timeline, name='timeline'),
    path('tooltipandpopover', tooltipandpopover, name='tooltipandpopover'),
    path('treeview', treeview, name='treeview'),
    path('typography', typography, name='typography'),
    path('users-list', users_list, name='users-list'),
    path('width', width, name='width'),
    path('wishlist', wishlist, name='wishlist'),
    path('wysiwyag', wysiwyag, name='wysiwyag'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)