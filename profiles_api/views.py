
import re
from urllib import request
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework import status
from profiles_api import serializers
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
             