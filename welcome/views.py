from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from welcome.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from welcome.models import Item, Question, Answer
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from .models import User
from .forms import LoginForm, RegisterForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from project import settings


@csrf_exempt
def index(request: HttpRequest) -> HttpResponse:
    """returns the number of objects in db to index url"""
    title = "My Cool App"
    return render(
        request, "welcome/spa/index.html", {"title": title,
                                            "n": User.objects.all().count()}
    )


def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(True)


def check(request: HttpRequest) -> HttpResponse:
    title = 'this is checking'
    return render(

        request, "welcome/spa/index1.html", {"title": title}
    )


@csrf_exempt
def users_api(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        # Checks if method is GET
        # returns all users requested
        userId = 1
        if request.user.is_authenticated:
            userId = request.user.id
        return JsonResponse({'users': [
            user.to_dict()
            for user in User.objects.all()
        ], 'id': userId})

    if request.method == 'POST':
        # Checks if method is POST
        # request body is returned as json data which will be passed as a python dictionary
        # Returns a list of users including the new one

        request = request.body.decode('utf-8')
        json_request = json.loads(request)
        user = User.objects.create(
            username=json_request['userName'],
            first_name=json_request['firstName'],
            last_name=json_request['lastName'],
            dob=json_request['dob'],
            email=json_request['email'],
            password=json_request['password'],
        )
        user.save()

        return JsonResponse({
            'users': [
                user.to_dict()
                for user in User.objects.all()
            ]
        })


@csrf_exempt
# user id gets passed to view function as an integar, this will be used for PUT and DELETE methods
def user_api(request: HttpRequest, id: int) -> HttpResponse:
    # view function retrieves song from database
    user = get_object_or_404(User, id=id)

    if request.method == 'GET':
        # Checks if method is GET
        # returns all user requested
        return JsonResponse(user.to_dict())

    if request.method == 'PUT':
        # Checks if method is PUT
        user = get_object_or_404(User, id=id)
        if request.method == "PUT":
            put = json.loads(request.body)
            user.username = put["username"]
            user.email = put["email"]
            user.first_name = put["first_name"]
            user.last_name = put["last_name"]
            user.image= put["image"]
            user.dob = put["dob"]

            user.save()
        return JsonResponse({"user": [user.to_dict()]})

    if request.method == 'DELETE':
        # Checks if method is DELETE
        user = get_object_or_404(User, id=id)
        user.delete()

        return JsonResponse({
            'users': [
                user.to_dict()
                for user in User.objects.all()
            ]
        })


@csrf_exempt
def register_view(request):
    '''
    register function, account creation
    '''
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # create a new user
            new_user = User.objects.create(username=username)
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.dob = form.cleaned_data['dob']
            new_user.email = form.cleaned_data['email']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # authenticate user
            # establishes a session, will add user object as attribute
            # on request objects, for all subsequent requests until logout
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                #auto email for registering
                subject = "Thank you for registering! " + username
                message = "welcome! Get ready to bid"
                from_email = settings.EMAIL_HOST_USER
                to_list = [new_user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=False)
                return redirect('http://localhost:8000/login/')

    return render(request, 'welcome/auth/register.html', {'form': RegisterForm})


@csrf_exempt
def login_view(request):
    '''
    Login function
    '''
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('http://localhost:5173/items/add')

            # failed authentication
            return render(request, 'error.html', {
                'error': 'User not registered. Sign up first.'
            })

        # invalid form
        return render(request, 'welcome/auth/login.html', {
            'form': form
        })

    return render(request, 'welcome/auth/login.html', {'form': form})


@login_required
def logout_view(request):
    auth.logout(request)
    return redirect('welcome:login')


@csrf_exempt
def items_api(request: HttpRequest):
    """if the req method is a GET, it returns a json object of all the
    item objects in the db. if the req method is a POST,it takes a request
    object and sets it to post. for each attribute in the object, itsets the
    right attribute of the Item model to the corresponding attribute from the
    request body.it then passes these attributes in and saves the item to the db.
    it returns a json repsonse"""
    if request.method == "GET":
        userId = 1
        if request.user.is_authenticated:
            userId = request.user.id
        return JsonResponse({"items": [item.to_dict() for item in Item.objects.all()], "user": userId})

    if request.method == "POST":
        POST = request.POST
        title = POST["title"]
        description = POST["description"]
        finishDate = POST["finishDate"]
        startingPrice = POST["startingPrice"]
        image = POST["image"]
        owner = POST["owner"]

        item = Item(
            title=title,
            description=description,
            finishDate=finishDate,
            startingPrice=startingPrice,
            image=image,
            owner=owner,
        )
        item.save()
        return JsonResponse({"items": [item.to_dict()]})


@csrf_exempt
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def upload_file(request: HttpRequest):
    if request.method == 'POST':
        img = request.FILES.get("file")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@csrf_exempt
def item_api(request: HttpRequest, item_id: int) -> HttpResponse:

    item = get_object_or_404(Item, id=item_id)
    if request.method == 'GET':
        return JsonResponse(item.to_dict())

    """it takes the request body and if the request method is PUTsets each attribute of the req object
    to the corresponding attribute of the Item object. it saves the changes to this entry. the put
    request is made to the specific API endpoint of the post the user is updating. this way the correct
    entry is. if the req method is delete, it deletes the entry from the db"""
    if request.method == 'PUT':
        form = UploadFileForm(request.POST, request.FILES)
        img = request.FILES
        return JsonResponse(item.to_dict())


@csrf_exempt
def questions_and_answers_api(request: HttpRequest):
    """if the req method is a GET, it returns a json object of all the
    question and answer objects in the db. if the req method is a POST,it takes a request
    object and sets it to post."""
    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("answer") == None:
            question = data.get("question")
            user = data.get("user")
            item = data.get("id")

            question = Question(
                question=question,
                user=user,
                item=item,
            )
            question.save()
            return JsonResponse({"question": [question.to_dict()]})
        else:
            questionId = data.get("question").get("id")
            question = Question.objects.get(pk=questionId)
            answer = data.get("answer").get("answer")
            user = data.get("answer").get("user")
            item = data.get("answer").get("id")

            answer = Answer(
                question=question,
                answer=answer,
                user=user,
                item=item,
            )
            answer.save()
            return JsonResponse({"answer": [question.answer.to_dict()]})

    if request.method == "GET":
        answer = []
        for question in Question.objects.all():
            try:
                answer.append(question.answer.to_dict())
            except ObjectDoesNotExist:
                answer.append(question.to_dict())
    return JsonResponse({"answers": answer})
