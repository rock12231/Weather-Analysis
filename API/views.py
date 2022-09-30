from django.shortcuts import render
from django.db import models
import pandas as pd
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from API.models import Snippet
from API.serializers import SnippetSerializer

df = pd.read_csv("API/data/dataexport.csv")

print(df.head())
class SnippetList(APIView):

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)