from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Assignment, Resource
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

assignments = Assignment.objects.all()
assignment_ids = []
for obj in assignments:
    assignment_ids.append(obj.id)

"""Workflows for managing assignments."""


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def assignment(request):
    """Assignments main page"""
    assignments = Assignment.objects.order_by('-published_date')
    context = {
        'assignments': assignments, 'assignment_ids': assignment_ids
    }
    return render(request, 'staff/assignment.html', context)


def add_assignment(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments': assignments, 'assignment_ids': assignment_ids
    }
    """Lecturers and staff to add assignments"""
    if request.method != 'POST':
        return render(request, 'staff/assignment.html', context)
    if request.method == 'POST':
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        # file = fss.save(upload.name, upload)
        # file_url = fss.url(file)
        assignment_title = request.POST.get('title', False)
        assignment_description = request.POST.get('description', False)
        assignment_uploads = upload
        assignment = Assignment(
            title=assignment_title, description=assignment_description,
            due_date=datetime.fromisoformat(request.POST.get('deadline')), uploads=assignment_uploads,
            program='RN'
        )
        assignment.save()
    return HttpResponseRedirect(reverse('routine:assignment'))

@csrf_exempt
def delete_assignment(request, pk):
    if request.method == 'POST' or request.method != 'POST':
        pk = int(pk)
        Assignment.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse('routine:assignment'))


def delete_all_assignments(request):
    if request.method == 'POST':
        Assignment.objects.all().delete()
        return HttpResponseRedirect(reverse('routine:assignment'))


def edit_assignment(request, pk):
    pk = int(pk)
    if request.method != 'POST':
        context = {
            'pk': pk, 'assignment': Assignment.objects.get(id=pk),
            'datetime': Assignment.objects.get(id=pk).due_date.isoformat()
        }
        return render(request, 'staff/edit_assignment.html', context)

    else:
        title = request.POST.get('title')
        description = request.POST.get('description', False)
        due_date = request.POST.get('deadline', False)
        uploads = request.FILES['upload']
        Assignment.objects.filter(id=pk).update(
            title=title, description=description, due_date=due_date, uploads=uploads
        )
        return HttpResponseRedirect(reverse('routine:assignment'))


#########################################################

"""Workflows for managing Resources"""


def resource(request):
    resources = Resource.objects.all()
    context = {
        'resources': resources
    }
    return render(request, 'staff/resource.html', context)


def edit_resource(request):
    return None


def announcements(request):
    return None