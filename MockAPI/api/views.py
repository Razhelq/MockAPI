from api.models import Account, Log
from api.serializers import AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse


class AccountListView(APIView):

    def get(self, request, format=None):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True, context={"request": request})
        response = Response(serializer.data)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            Log.objects.create(request=request.get_full_path, response=response)
            return response
        response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response


class AccountView(APIView):

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        account = self.get_object(id)
        serializer = AccountSerializer(account, context={"request": request})
        response = Response(serializer.data)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def delete(self, request, id, format=None):
        account = self.get_object(id)
        account.delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def put(self, request, id, format=None):
        account = self.get_object(id)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data)
            Log.objects.create(request=request.get_full_path, response=response)
            return response
        response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def post(self, request, id, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            Log.objects.create(request=request.get_full_path, response=response)
            return response
        response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response


class ProductBuyView(APIView):

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def post(self, request, id, price, format=None):
        account = self.get_object(id)
        account.balance -= int(price)
        account.save()
        response = Response(status=status.HTTP_201_CREATED)
        Log.objects.create(request=request.get_full_path, response=response)
        return HttpResponse('Produkt został zakupiony')



class WrongEndpointView(APIView):

    def get(self, request, format=None):
        response = Http404
        Log.objects.create(request=request.get_full_path, response=response)
        raise Http404

    def delete(self, request, format=None):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def put(self, request, format=None):
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def post(self, request, format=None):
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response

    def patch(self, request, format=None):
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        Log.objects.create(request=request.get_full_path, response=response)
        return response
