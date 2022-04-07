
import re
from urllib import request
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
# Create your views here.
class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer

    def get(self ,requst,format=None):
        an_apiview=[
            'Uses HTTP methods as function (get ,post , patch , put ,delete)',
            'IS similar to a teriditional django View',
            'Gives you the most control over your application logic',
            'is mapped manually to Urls',


        ]
        return Response({'message':"hello","an_apiview":an_apiview })


    def post(self,request):
       
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f"Hello {name}"
            return Response({"message":message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

  
    def patch(self ,request , pk=None):
        return Response({"method" :"PATCH"})

    def delete(self ,request ,pk=None):
        return Response({"method":"DELETE"})

    def put(self ,request ,pk=None):
        return Response({ "method":"PUT" })


class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self ,request):

        a_viewset=[
            'user action (list , create ,retrive ,update ,partial update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionalty with less code',
        ]
        return Response({'message' :'hello!' , 'a_viewset': a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}!"
            return Response({'message':message})
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
        
    def update(self ,request ,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'htp_method':'PATCH'})
        
    def destroy(self ,request,pk=None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnPorifle,)