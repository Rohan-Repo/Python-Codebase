from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

# movieData ={
#     'movies': [
#         {
#             'id': 1,
#             'title': 'Mission Impossible',
#             'year': 2000 
#         },
#         {
#             'id': 2,
#             'title': 'Incredible Hulk',
#             'year': 2001 
#         },
#         {
#             'id': 3,
#             'title': 'Iron Man',
#             'year': 2008 
#         }
#     ]
# }

def movies(request):
    movieData = Movie.objects.all()
    # This returns an error : context must be a dict rather than QuerySet.
    # Cause it expects it to be a Dictionary Obj so just create one
    # return render( request, 'movies/movies.html', movieData )
    return render( request, 'movies/movies.html', {'movies':movieData} )

def home(request):
    return HttpResponse("home() function")

def movieDetail(request, id):
    data = Movie.objects.get(pk=id)
    return render( request, 'movies/moviedetail.html', {'movie': data} )

# def addMovie(request):
#     # Get Values from our addmovie form
#     # Ensure these names match the ones from our HTML 
#     movieYear = request.POST.get('movieYear')
#     movieName = request.POST.get('movieName')

#     # If both values have been sent we create a Movie Object
#     if movieYear and movieName:
#         movie = Movie( title=movieName, year=movieYear )
#         # To save the details to DB
#         movie.save()
#         # Once it saves Redirect to our home page
#         return HttpResponseRedirect( '/movies')
#     return render(request, 'movies/addmovie.html')

def addMovie(request):
    # Get Values from our addmovie form
    # Ensure these names match the ones from our HTML 
    movieYear = request.POST.get('movieYear')
    movieName = request.POST.get('movieName')

    try:
        # If both values have been sent we create a Movie Object
        if movieYear and movieName:
            movie = Movie( title=movieName, year=movieYear )
            # To save the details to DB
            movie.save()
            # Once it saves Redirect to our home page
            return HttpResponseRedirect( '/movies')
    except:
        raise Http404('Incorrect Details Entered')
    
    return render(request, 'movies/addmovie.html')

def deleteMovie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie ID Does not exist' )
    # If Movie ID is found Delete it and Redirect
    movie.delete()
    return HttpResponseRedirect( '/movies' )