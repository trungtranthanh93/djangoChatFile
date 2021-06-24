import pyrebase
from django.http import HttpResponse, JsonResponse

config = {
    'apiKey': "AIzaSyDbY2FYw8w4YhCaGl9s-8EKqBK_J1B4XOc",
    'authDomain': "djangoapp-8251e.firebaseapp.com",
    'databaseURL': "https://djangoapp-8251e-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "djangoapp-8251e",
    'storageBucket': "djangoapp-8251e.appspot.com",
    'messagingSenderId': "381033511814",
    'appId': "1:381033511814:web:353dc0cf764e8c0ac94a07",
    'measurementId': "G-6830N40FKY"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()
user = auth.sign_in_with_email_and_password('test1@ttt.com', '123456')
token = auth.create_custom_token("abc123")
user = auth.refresh(user['refreshToken'])
userIdToken = user['idToken']
# Create your views here.
def index(request):
    data = {
        'id': database.child('data').child('id').get().val(),
        'name': database.child('data').child('name').get().val(),
        'projectName': database.child('data').child('projectname').get().val()
    }
    return JsonResponse(data)

#create data with unique, auto-generated, timestamp-based key
def push(request):
    data = {
        'name': 'Trung',
        'id': '1'
    }
    database.child("users").push(data,userIdToken)
    return HttpResponse("success")
#create data with own keys
def set(request):
    data = {
        'name': 'Trung',
        'id': '2'
    }
    database.child("users").child("own keys").set(data)
    return HttpResponse("success")

#update data wit own keys
def update(request):
    database.child("users").child("own keys").update({"name":'Trung1'})
    return HttpResponse("success")


#multi-location updates
def updateMutilLocation(request):
    data = {
        "users/Trung/": {
            "name": "Trung update v1"
        },
        "users/Tran/": {
            "name": "Tran update v1"
        }
    }
    database.update(data)
    return HttpResponse("success")


def updateMutilLocationWithGenerateKey(request):
    data = {
        "users/" + database.generate_key(): {
            "name": "Trung v2 GenerateKey"
        },
        "users/" + database.generate_key(): {
            "name": "Trung v2 GenerateKey"
        }
    }
    database.update(data)
    return HttpResponse("success")

#upload image
def uploadImage(request):
    storage.child("image1").put("C:/Users/trung/Downloads/2.jpg", userIdToken)
    return HttpResponse("success")