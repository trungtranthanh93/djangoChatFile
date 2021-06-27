import datetime

import firebase_admin
from firebase_admin import credentials, firestore
from django.http import HttpResponse, JsonResponse

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-project-trungtt.firebaseio.com'
})

db = firestore.client()

# Create your views here.
def index(request):
    data = db.collection(u'cities').get()
    return JsonResponse(data)


# create data with unique, auto-generated, timestamp-based key
def push(request):
    data = {
        u'name': u'Los Angeles',
        u'state': u'CA',
        u'country': u'USA'
    }

    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection(u'cities').document(u'LA').set(data)
    return HttpResponse("success")

# create data with own keys
def set(request):
    data = {
        u'stringExample': u'Hello, World!',
        u'booleanExample': True,
        u'numberExample': 3.14159265,
        u'dateExample': datetime.datetime.now(),
        u'arrayExample': [5, True, u'hello'],
        u'nullExample': None,
        u'objectExample': {
            u'a': 5,
            u'b': True
        }
    }
    db.collection(u'data').document(u'one').set(data)
    return HttpResponse("success")


# update data wit own keys
def update(request):
    db.child("users").child("own keys").update({"name": 'Trung1'})
    return HttpResponse("success")


# multi-location updates
def updateMutilLocation(request):
    data = {
        "users/Trung/": {
            "name": "Trung update v1"
        },
        "users/Tran/": {
            "name": "Tran update v1"
        }
    }
    db.update(data)
    return HttpResponse("success")


def updateMutilLocationWithGenerateKey(request):
    data = {
        "users/" + db.generate_key(): {
            "name": "Trung v2 GenerateKey"
        },
        "users/" + db.generate_key(): {
            "name": "Trung v2 GenerateKey"
        }
    }
    db.update(data)
    return HttpResponse("success")


# upload image
def uploadImage(request):
    # storage.child("image1").put("C:/Users/trung/Downloads/2.jpg")
    return HttpResponse("success")
