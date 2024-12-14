from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import HelloSerializer 
from profiles_api import models
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



class HelloApiView(APIView):
    """Test Api view"""

    serializer_class = HelloSerializer
    
    def get(self, request, format=None):
        """Return a list of api view"""
        
        an_apiview = [
            'use http methode as function (get , post, patch, put, delete)',
            'Is Similar to traditional Django view',
            'Give you the most control oer your application logic',
            'is mapped manually to URLS'
        ]
        return Response({'Message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Cerate a hello message with your name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, pk=None):
        """Handel Updating an Object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handel  pratial update an Object"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})





    
class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    serializer_class = HelloSerializer

    def list(self, request):
        """REturn Hello Message"""
        
        a_viewset = [
            'Uses actions (list , create, retrive update , partial_update)',
            'Automaticly maps to Urls Usinfg Routers',
            'provides more functionality with less code'
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    
    def create(self, request):
        """Create an new Hello Message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Hande gettinf an object by its id """
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Handel Updating An Object"""
        return Response({'http_method':'PUT'})
    
    
    def partial_update(self, request, pk=None):
        """Handling Updating part of project"""
        return Response({'http_method':'PATCH'})
    
    
    def destroy(self, request, pk=None):
        """Handel Removing an Object"""
        return Response({'http_method':'DELETE'})
    
    
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel Creating and Updating Profile"""
    
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = [filters.SearchFilter,]
    search_fildes = ['name', 'email']



class UserLoginApiView(ObtainAuthToken):
    """Handel creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES