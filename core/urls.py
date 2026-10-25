from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 教师页面
    path('teacher/', views.teacher_home, name='teacher_home'),
    path('teacher/group/<int:group_id>/', views.teacher_group_detail, name='teacher_group_detail'),
    path('teacher/student/<int:student_id>/', views.teacher_student_detail, name='teacher_student_detail'),

    # 学生页面
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/profile/edit/', views.student_profile_edit, name='student_profile_edit'),

    # 管理员页面
    path('manage/students/', views.admin_students, name='admin_students'),
    path('manage/teachers/', views.admin_teachers, name='admin_teachers'),
    path('manage/groups/', views.admin_groups, name='admin_groups'),
    path('manage/students/assign/', views.admin_assign_student, name='admin_assign_student'),
]