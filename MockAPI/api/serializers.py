from rest_framework import serializers
from api.models import Person, Account


class AccountSerializer(serializers.ModelSerializer):
    person = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.all())

    class Meta:
        model = Account
        fields = ("balance", "person")
