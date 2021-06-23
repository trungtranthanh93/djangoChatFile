import pyrebase
from django.http import HttpResponse, JsonResponse
config={
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
# Create your views here.
def index(request):
    data = {
        'id': database.child('data').child('id').get().val(),
        'name': database.child('data').child('name').get().val(),
        'projectName': database.child('data').child('projectname').get().val()
    }
    return JsonResponse(data)
