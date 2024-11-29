from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    
    """Test Api view"""


    def get(self, request, format=None):
        """Return a list of api view"""
        an_apiview = [
            'use http methode as function (get , post, patch, put, delete)',
            'Is Similar to traditional Django view',
            'Give you the most control oer your application logic',
            'is mapped manually to URLS'
        ]

        return Response({'Message':'Hello', 'an_apiview':an_apiview})
