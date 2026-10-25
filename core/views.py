from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Страница входа (в разработке)")

def logout_view(request):
    return HttpResponse("Выход из системы (в разработке)")

def teacher_home(request):
    return HttpResponse("Главная страница преподавателя: Список групп (в разработке)")

def teacher_group_detail(request, group_id):
    return HttpResponse(f"Информация о группе, ID={group_id} (в разработке)")

def teacher_student_detail(request, student_id):
    return HttpResponse(f"Карточка студента, ID={student_id} (в разработке)")

def student_profile(request):
    return HttpResponse("Личная страница студента (в разработке)")

def student_profile_edit(request):
    return HttpResponse("Редактирование контактных данных (в разработке)")

def admin_students(request):
    return HttpResponse("Управление студентами (в разработке)")

def admin_teachers(request):
    return HttpResponse("Управление преподавателями (в разработке)")

def admin_groups(request):
    return HttpResponse("Управление группами (в разработке)")

def admin_assign_student(request):
    return HttpResponse("Распределение студентов по группам (в разработке)")