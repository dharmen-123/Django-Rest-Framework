from .models import Student

class StudentSerializer(serializers.ModelSerializers):
    class Meta:
        model='Student'
        fields='__all__'