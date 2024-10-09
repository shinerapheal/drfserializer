from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def view(request):
    if request.method=='GET':
        obj=people.objects.all()
        serializers=PeopleSerializer(obj,many=True)

        return Response(serializers.data)
    elif request.method=='POST':
        data=request.data
        serializers=PeopleSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
    elif request.method=='PUT':
        data=request.data
        obj=people.objects.get(id=data['id'])
        serializers=PeopleSerializer(obj,data=data)  
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data) 
    elif request.method=='DELETE':
        data=request.data
        obj=people.objects.get(id=data['id']) 
        obj.delete()
        return Response({"message":"deleted"})    

