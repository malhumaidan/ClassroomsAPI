from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ClassroomForm
from .models import Classroom


def classroom_list(request):
    classrooms = Classroom.objects.all()
    context = {
        "classrooms": classrooms,
    }
    return render(request, "classroom_list.html", context)


def classroom_detail(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    context = {
        "classroom": classroom,
    }
    return render(request, "classroom_detail.html", context)


def classroom_create(request):
    form = ClassroomForm()
    if request.method == "POST":
        form = ClassroomForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Created!")
            return redirect("classroom-list")
        print(form.errors)
    context = {
        "form": form,
    }
    return render(request, "create_classroom.html", context)


def classroom_update(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    form = ClassroomForm(instance=classroom)
    if request.method == "POST":
        form = ClassroomForm(request.POST, request.FILES or None, instance=classroom)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited!")
            return redirect("classroom-list")
        print(form.errors)
    context = {
        "form": form,
        "classroom": classroom,
    }
    return render(request, "update_classroom.html", context)


def classroom_delete(request, classroom_id):
    Classroom.objects.get(id=classroom_id).delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("classroom-list")
