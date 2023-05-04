from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Animals, Type
from .serializers import AnimalsSerializer, TypeSerializer


class TypeAPIView(APIView):
    def get(self, request):
        a = Type.objects.all()
        return Response({'type': TypeSerializer(a, many=True).data})

    def post(self, request):
        serializer2 = TypeSerializer(data=request.data)
        serializer2.is_valid(raise_exception=True)
        post_new2 = Type.objects.create(
            name_type=request.data['name_type'])
        return Response(
            {'type': TypeSerializer(post_new2).data},
        )


class TypeAPIList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeAPIUpdate(generics.UpdateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class AnimalsAPIView(APIView):
    def get(self, request):
        a = Animals.objects.all()

        return Response({'animals': AnimalsSerializer(a, many=True).data})


    def post(self, request):
        serializer = AnimalsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'animals': serializer.data},
        )


class AnimalsAPIList(generics.ListCreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer


class AnimalsAPIUpdate(generics.UpdateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer


class AnimalsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer
