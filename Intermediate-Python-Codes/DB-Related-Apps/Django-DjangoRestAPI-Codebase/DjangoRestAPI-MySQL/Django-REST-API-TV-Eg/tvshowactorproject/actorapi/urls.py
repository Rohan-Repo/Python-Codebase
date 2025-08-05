from django.urls import path
from .views import getActorData,createActor, singleUserOperations

urlpatterns = [
    path( 'actors/', getActorData, name='getActorData' ),
    path( 'actor/create', createActor, name='createActor' ),
    path( 'actor/<int:id>', singleUserOperations, name='singleUserOperations' ),
]