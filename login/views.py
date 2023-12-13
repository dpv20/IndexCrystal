from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from django.http import JsonResponse
from .models import ExternalWebpageUser
from django.conf import settings
import os


def index(request):
    return render(request, 'login/index.html')


def root_page(request):
    return render(request, 'login/root_page.html')


@login_required
def upload_profile_picture(request):
    if request.method == 'POST' and request.FILES['profile_pic']:
        employee = Employee.objects.get(email=request.user.username)

        # If there's an existing profile picture, delete it
        if employee.profile_pic:
            existing_path = employee.profile_pic.path
            if os.path.isfile(existing_path):
                os.remove(existing_path)

        # Save the new profile picture
        employee.profile_pic = request.FILES['profile_pic']
        employee.save()

        # Prepare the context with updated data
        full_name = employee.full_name
        profile_pic_url = employee.profile_pic.url if employee.profile_pic else None
        context = {
            'user': request.user,
            'full_name': full_name,
            'profile_pic_url': profile_pic_url,
        }

        return render(request, 'login/root_page.html', context)

    return redirect('root_page')

@login_required
def root_page(request):
    try:
        # Retrieve the Employee object that has the email matching the logged-in user's username
        employee = Employee.objects.get(email=request.user.username)
        full_name = employee.full_name
        # Check if profile_pic exists for the employee
        profile_pic_url = employee.profile_pic.url if employee.profile_pic else None
    except Employee.DoesNotExist:
        # If no matching employee is found, use default values
        full_name = "No name available"  # or use request.user.username
        profile_pic_url = None  # or URL to a default image

    # Pass the full_name and profile_pic_url to the template
    context = {
        'user': request.user,
        'full_name': full_name,
        'profile_pic_url': profile_pic_url,
    }
    return render(request, 'login/root_page.html', context)