from rest_framework import serializers

from DjangoMedicalApp.models import Company



class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model=Company
        # fields="__all__"
        fields=["name","license_no","address","contact_no","email","description"]