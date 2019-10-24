from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, \
    BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """ use authentication classes here to use powerful authentication mechanism
    provided by rest framework.
    """
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {'status': status.HTTP_201_CREATED,
                        'content': serializer.data}
            return Response(response)
