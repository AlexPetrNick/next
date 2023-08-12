from rest_framework import viewsets, mixins, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from version1.serializers import *


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False)
    def send_message_push(self, request):
        return Response({'hello': 'hello'})

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            print("GET")
            return self.serializer_class
        print("POST")
        return UserSerializerPost


class MovieAPIViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class StatusCodeAPIViewSet(viewsets.ModelViewSet):
    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer


class FeedbackAPIViewSet(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer


class HeadersView(mixins.ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"headers": request.headers})


class IpView(mixins.ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"ip": request.META["REMOTE_ADDR"]})


