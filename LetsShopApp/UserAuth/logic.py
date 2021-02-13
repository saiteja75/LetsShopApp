from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def registerTheUser(request):
    userName = request.POST.get('UserName')
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    emailId = request.POST.get('email')
    password = request.POST.get('psw')
    try:
        user = User(username = userName, password = password, email = emailId, first_name = firstName, last_name = lastName)
        user.save(user.password)
        user.set_password(password)
        user.save()
        return True
    except:
        return False

def authenticateUser(request):
    userName = request.POST.get('username')
    password = request.POST.get('password')
    print(userName)
    print(password)
    user = authenticate(username= userName, password= password)
    print(user)
    if user is not None:
        login(request, user)
    return user

def logoutUser(request):
    logout(request)
    