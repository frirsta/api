from rest_framework import serializers
from .models import Test, TesterResult, TestRequirements, User, Result


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name',
        'password', 'password2',]
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            is_tutor=self.validated_data['is_tutor'],
            is_student=self.validated_data['is_student'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
    


class TestRequirementsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='client.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TestRequirements
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TesterResultSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='tester.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TesterResult
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
