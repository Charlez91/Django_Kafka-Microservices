from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, 
                                   validators = [UniqueValidator(queryset=User.objects.all(), message={"email": "Email already taken"})])
    
    password = serializers.CharField(write_only= True, required= True, validators = [validate_password])
    password2 = serializers.CharField(write_only= True, required= True,)  

    class Meta:
        model = User
        fields = ["email", "password", "password", "firstname", "lastname", "username"]
        extra_kwargs = {
            "firstname": {"required": True},
            "lastname": {"required": True}
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password":"Password Field didnt match!."})
        
        #return attrs
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(raw_password=validated_data["password"])
        user.save()
                 