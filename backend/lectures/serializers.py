from rest_framework import serializers
from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    """講義シリアライザー"""

    class Meta:
        model = Lecture
        fields = [
            'id',
            'lecture_name',
            'professor_name',
            'category',
            'credit_level',
            'semester',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
