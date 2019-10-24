from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """TODO: Need to import User model class."""
        model = User
        fields = ('email', 'password', 'comment',)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()
        return user
