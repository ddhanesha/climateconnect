from rest_framework import serializers
from chat_messages.models.message import Message
from climateconnect_api.models import UserProfile
from climateconnect_api.serializers.user import UserProfileStubSerializer

from climateconnect_api.models import (
    Notification, UserNotification
)
from chat_messages.serializers.message import MessageSerializer
from organization.serializers.content import ProjectCommentSerializer

class NotificationSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    chat_uuid = serializers.SerializerMethodField()
    chat_title = serializers.SerializerMethodField()
    project_comment = serializers.SerializerMethodField()
    project_comment_parent = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()
    project_follower = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'id',
            'notification_type',
            'text',
            'last_message',
            'chat_uuid',
            'chat_title',
            'project_comment',
            'project_comment_parent',
            'project',
            'project_follower'
        )
    
    def get_last_message(self, obj):
        message_participant = obj.chat
        if obj.chat:
            last_message = Message.objects.filter(message_participant=message_participant).first()
            serializer = MessageSerializer(last_message, many=False, context=self.context)
            return serializer.data
        else:
            return None
    
    def get_chat_uuid(self, obj):
        if obj.chat:
            return obj.chat.chat_uuid
        else:
            return None

    def get_chat_title(self, obj):
        if obj.chat:
            return obj.chat.name
        else:
            return None

    def get_project_comment(self, obj): 
        if obj.project_comment:
            serializer = ProjectCommentSerializer(obj.project_comment)
            return serializer.data

    def get_project_comment_parent(self, obj): 
        if obj.project_comment:
            serializer = ProjectCommentSerializer(obj.project_comment.parent_comment)
            return serializer.data

    def get_project(self, obj):
        if obj.project_comment:
            return {
                "name": obj.project_comment.project.name,
                "url_slug": obj.project_comment.project.url_slug
            }
        if obj.project_follower:
            return {
                "name": obj.project_follower.project.name,
                "url_slug": obj.project_follower.project.url_slug
            }

    def get_project_follower(self, obj):
        if obj.project_follower:
            follower_user = UserProfile.objects.filter(user=obj.project_follower.user)
            serializer = UserProfileStubSerializer(follower_user[0])
            return serializer.data