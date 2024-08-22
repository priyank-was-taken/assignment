from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, decorators, login, logout
from .models import fileUpload



# home page or upload page.......
@decorators.login_required(login_url='login')
def home(request):
    context = {}
    if request.method == 'POST':
        try:
            file = request.FILES['file']
        except:
            context = {'error': 'No file selected'}
            return render(request, 'index.html', context)
        if file:
            fileUpload.objects.create(file=file, user=request.user)
        print('The file is ', file)
    return render(request, 'index.html', {'error': ''})





#user login.....
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')




# user signup
def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if models.User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = models.User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('/')

    return render(request, 'signup.html')


# logout view
@decorators.login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


# list of files....
@decorators.login_required(login_url='login')
def list(request):
    data = fileUpload.objects.filter(user=request.user)
    absolute_urls = []
    for file in data:
        file.absolute_url = request.build_absolute_uri(file.file.url)

    print(data)
    return render(request, 'listpage.html', {'items': data})


# delete the files....
@decorators.login_required(login_url='login')
def delete(request):
    id = request.GET.get('id')
    print('The id is', id)
    data = fileUpload.objects.get(id=id).delete()
    return redirect('list')
