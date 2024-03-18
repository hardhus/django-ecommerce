from rest_framework import serializers
from djangular_pools.models import Poll, PollItem

class PollItemSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()
    class Meta:
        model = PollItem
        fields = ('id', 'poll', 'name', 'text', 'votes', 'percentage')

    def get_percentage(self, obj):
        return obj.percentage 

class PollSerializer(serializers.ModelSerializer):
    items = PollItemSerializer(many=True, required=False)
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ('id', 'title', 'publish_date', 'items', 'total_votes')

    def get_total_votes(self, obj):
        return obj.total_votes