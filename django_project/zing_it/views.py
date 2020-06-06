from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import Signup,Login

# Create your views here.



my_songs = [
            {"id": 1, "Track": "thank u, next", "Artist": "Ariana Grande", "Album": "thank u, next", "Length": "3:27","playlist_id": 1},
            {"id": 2, "Track": "One Kiss, next", "Artist": "Dua Lipa, Calvin Harris", "Album": "One Kiss", "Length": "3:34","playlist_id": 1},
            {"id": 3, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51","playlist_id": 1},
            {"id": 4, "Track": "The Middle", "Artist": "Grey,Marren Morris, ZEDD", "Album": "The Middle", "Length": "3:04","playlist_id": 1},
            {"id": 5, "Track": "Love Lies", "Artist": "Normani, Khalid", "Album": "Love Lies", "Length": "3:21","playlist_id": 2},
            {"id": 6, "Track": "Rise", "Artist": "Jack & Jack, Jonas Blue", "Album": "Blue", "Length": "3:14","playlist_id": 2},
        ]

my_playlists=[
    {"id":1,"name":"Car Playlist","numberOfSongs":4},
    {"id":2,"name":"Coding Playlist","numberOfSongs":2}
]

users = [
            {"id": 1, "full_name": "john", "email": "john123@gmail.com", "password": "adminpass"},
        ]


def home(request):
    
    # music_types=['Pop','Rock','R&B','Soul & Funk','Blues','Reggae','Soundtracks','Dance & EDM','Rap', 'Asian Music','Jazz','Kpop','Metal','Electronic','Classical']
    return render(request,'zing_it/home.html',{"my_playlists":my_playlists})


def about(request):
    return HttpResponse("""<h1>About Us:</h1><p>With Zing, you can easily find the music of your choice and easily share it with other people. You can also browse through the collections of friends, artists, and celebrities, or create a playlist of your own.
      Soundtrack your life with Zing. Subscribe or listen for free.</p>""")

def playlist(request,id):
    songs=[]
    playlist_name=''
    for playlist in my_playlists:
        if(id == playlist['id']):
            playlist_name=playlist['name']

    if len(playlist_name)==0:
        raise Http404("Such playlist does not exist")

    for song in my_songs:
        if(id == song['playlist_id']):
            songs.append(song)
        
    return render(request,'zing_it/songs.html',{"songs":songs,"playlist_name": playlist_name})

def signup(request):
    form = Signup(request.POST or None)
    if form.is_valid():
        password= form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        print(email)
        if(password!= confirm_password):
            return render(request,'zing_it/signup.html',{"form":form,"status":"Your passwords don't match!"})
        else:
            print("this is:",email)
            try:
                user= User.objects.get(email=email)
                return render(request,'zing_it/signup.html',{"form":form,"status":"This email already exists in the system! Please log in instead."})
            except Exception as e:
                print(e)
                new_user = User.objects.create_user(username= name, email= email,password= password)
                new_user.save()
                return render(request,'zing_it/signup.html',{"form":form,"status":"Signed up Successfully!"})
    return render(request,'zing_it/signup.html',{"form":form})

def login(request):
    form = Login(request.POST or None)
    status= " "
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = next((user for user in users if user["email"] == email and user["password"] == password), None)
        if user:
            status="Successfully logged in!"
        else:
            status="Wrong Credentials!"
    return render(request,'zing_it/login.html',{"form":form,"status":status})

    