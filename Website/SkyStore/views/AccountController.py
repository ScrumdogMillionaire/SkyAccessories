__author__ = 'bog02'

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User




# def create_login(request):
#     if request.method == 'POST':
#         username = request.POST['email']
#         password = request.POST['password']
#
#         # check if user already exists
#         if not User.objects.get(username__exact=username):
#             user = User.objects.create_user(username, password)
#             user.save()
#
#
# def create_guest_login(request):
#     pass
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # redirect to account page
#
#             else:
#                 return 'disabled account message'
#
#         else:
#             return 'invalid login message'
#
#
# def change_password():
#     pass
#
#
# def logout(request):
#     logout(request)
#
#
# def home(request):
#     return render(request, "home.html", {'name': 'ScrumdogMillionaires', 'user' : User})
#

