__author__ = 'bog02'


def create_user():
    pass


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


def change_password():
    pass


def logout():
    pass


