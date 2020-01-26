from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

music_types=[
            { "id": "1","name" : "Pop"}, { "id": "2","name" : "Rock"}, { "id": "3","name" : "R&B"}, { "id": "4","name" : "Soul & Funk"}, { "id": "5","name" : "Blues"}
    ]

biggest_hits_2018 = [
            {"id": 1, "Track": "thank u, next", "Artist": "Ariana Grande", "Album": "thank u, next", "Length": "3:27"},
            {"id": 2, "Track": "One Kiss, next", "Artist": "Dua Lipa, Calvin Harris", "Album": "One Kiss", "Length": "3:34"},
            {"id": 3, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51"},
            {"id": 4, "Track": "The Middle", "Artist": "Grey,Marren Morris, ZEDD", "Album": "The Middle", "Length": "3:04"},
            {"id": 5, "Track": "Love Lies", "Artist": "Normani, Khalid", "Album": "Love Lies", "Length": "3:21"},
            {"id": 6, "Track": "Rise", "Artist": "Jack & Jack, Jonas Blue", "Album": "Blue", "Length": "3:14"},
        ]


def home(request):
    
    # music_types=['Pop','Rock','R&B','Soul & Funk','Blues','Reggae','Soundtracks','Dance & EDM','Rap', 'Asian Music','Jazz','Kpop','Metal','Electronic','Classical']
    return render(request,'zing_it/home.html',{"music_types":music_types})


def about(request):
    return HttpResponse("""<h1>About Us:</h1><p>With Zing, you can easily find the music of your choice and easily share it with other people. You can also browse through the collections of friends, artists, and celebrities, or create a playlist of your own.
      Soundtrack your life with Zing. Subscribe or listen for free.</p>""")

def music(request,id):
    # music_types=[
    #         { "id": "1","name" : "Pop"}, { "id": "2","name" : "Rock"}, { "id": "3","name" : "R&B"}, { "id": "4","name" : "Soul & Funk"}, { "id": "5","name" : "Blues"},
    #         { "id": "6","name" : "Reggae"}, { "id": "7","name" : "Soundtracks"}, { "id": "8","name" : "EDM"}, { "id": "9","name" : "Rap"}, { "id": "10","name" : "Asian Music"},
    #         { "id": "11","name" : "Jazz"}, { "id": "12","name" : "Kpop"}, { "id": "13","name" : "Metal"}, { "id": "14","name" : "Electronic"}, { "id": "15","name" : "Classical"},
    # ]
    print(id)
    for type in music_types:
        if type["id"] == id:
            return render(request,'zing_it/music_type.html',{"music": type,"songs":biggest_hits_2018})
    