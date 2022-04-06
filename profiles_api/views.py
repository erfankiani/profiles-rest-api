
from rest_framework.views import APIView
from rest_framework.response  import Response
 
# Create your views here.
class HelloApiView(APIView):
    def get(self ,requst,format=None):
        an_apiview=[
            'Uses HTTP methods as function (get ,post , patch , put ,delete)',
            'IS similar to a teriditional django View',
            'Gives you the most control over your application logic',
            'is mapped manually to Urls',


        ]
        return Response({'message':"hello","an_apiview":an_apiview })