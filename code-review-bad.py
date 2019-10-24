# Remove relativedelta import, not used anywhere
from dateutil.relativedelta import relativedelta

from rest_framework import viewsets

# Remove *, Import always required classes/methods instead importing all using(*)
from rest_framework.response import *

# Remove json import, not used anywhere
import json

# Class name UsersViewSet should be UserViewSet.
# UserSerializer not imported from serializers.py
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# Indentation error
def create(self, request):
        # Didn't use authentication classes.
        if not request.user.is_authenticated():
            return Response("You should be authenticated")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Serializers should be handle user creation.
            comment = request.POST["comment"]
            user = User.objects.create(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                # Parenthesis missing
                comment=comment,
            # response status code is hard coded, instead used from status module    
            response = {'code': 200, 'success': True, 'id': user.id}
            return Response(response)
        # Useless else part, due to not using authetication classes.
        else:
            print ('error on the creation')
            return Response('error')