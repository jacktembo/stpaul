from django.shortcuts import render


def announcements(request):
    return render(request, 'general/announcements.html')