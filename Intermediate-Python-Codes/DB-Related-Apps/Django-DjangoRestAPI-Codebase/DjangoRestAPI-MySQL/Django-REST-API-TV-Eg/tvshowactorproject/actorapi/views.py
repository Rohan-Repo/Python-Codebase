# from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TVShowActorsModel
from .serializer import ActorSerializer

# Method to Return All Actor Data
@api_view( ['GET'])
def getActorData(request):
    # This was the dummy Data
    # return Response( ActorSerializer( {'showName':'Friends', 'actorShowName':'Chandler Bing', 'actorRealName': 'Matthew Perry'} ).data )
    # We want all of the objects
    actorData = TVShowActorsModel.objects.all()
    serializer = ActorSerializer( actorData, many=True )
    return Response( serializer.data )

# Method to Create Actor Data
@api_view( ['POST'])
def createActor(request):
    # Serialize Request Data 
    serializer = ActorSerializer( data=request.data )

    # If Data is Valid Save Data to DB and send 201 Status Code 
    if serializer.is_valid():
        serializer.save()
        return Response( 'User Successfully Created!', status=status.HTTP_201_CREATED )
    # If any Error raised send that back with a 400 Status Code
    else:
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

# Method to Select/Update/Delete Single Actor Data
@api_view( ['GET', 'PUT', 'DELETE'] )
def singleUserOperations( request, id ):
    # Check if User exists in the DB
    try:
        actor = TVShowActorsModel.objects.get( pk=id )
    except TVShowActorsModel.DoesNotExist:
        return Response( 'User Not Found!', status=status.HTTP_404_NOT_FOUND )
    
    # If User exists and Request is for View [GET]
    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response( serializer.data, status=status.HTTP_200_OK )
    
    # If User exists and Request is for Update [PUT]
    elif request.method == 'PUT':
        serializer = ActorSerializer( actor, data=request.data )
        # If Data is valid update it in the DB
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_202_ACCEPTED )
        # If any Error raised send that back with a 400 Status Code
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        
    # If User exists and Request is for removing [DELETE]
    elif request.method == 'DELETE':
        actor.delete()
        return Response( 'User was Deleted!', status=status.HTTP_204_NO_CONTENT )    
    # If User method is neither of GET, PUT or DELETE
    else:
        return Response( 'Incorrect Method!', status=status.HTTP_405_METHOD_NOT_ALLOWED )

