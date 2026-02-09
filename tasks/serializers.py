from rest_framework import serializers
from django.contrib.auth import get_user_model
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    assigned_to_email = serializers.EmailField(write_only=True, required=False)
    
    creator_details = serializers.SerializerMethodField(read_only=True)
    assigned_to_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "status", "due_date",
            "assigned_to", "assigned_to_email", 
            "creator", "created_at",
            "creator_details", "assigned_to_details"
        ]
        read_only_fields = ["id", "creator", "created_at", "assigned_to"]

    def get_creator_details(self, obj):
        return {"email": obj.creator.email, "id": obj.creator.id}

    def get_assigned_to_details(self, obj):
        if obj.assigned_to:
            return {"email": obj.assigned_to.email, "id": obj.assigned_to.id}
        return None

    def create(self, validated_data):
        
        assigned_email = validated_data.pop("assigned_to_email", None)
        
        if assigned_email:
            User = get_user_model()
            try:
                user = User.objects.get(email=assigned_email)
                validated_data["assigned_to"] = user
            except User.DoesNotExist:
                raise serializers.ValidationError({"assigned_to_email": "User with this email does not exist."})
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        
        assigned_email = validated_data.pop("assigned_to_email", None)
        
        if assigned_email:
            User = get_user_model()
            try:
                user = User.objects.get(email=assigned_email)
                instance.assigned_to = user
            except User.DoesNotExist:
                raise serializers.ValidationError({"assigned_to_email": "User does not exist."})
        
        return super().update(instance, validated_data)