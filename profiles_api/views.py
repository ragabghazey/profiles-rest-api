from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer  # استيراد الـ Serializer
from rest_framework import status


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
        """Handel Updapratial update tiofng an Object"""
        return Response({'method':'PATCH'})

    
    
    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})

    
    
    
    
    
    