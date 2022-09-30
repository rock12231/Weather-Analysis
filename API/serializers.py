from rest_framework import serializers

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(required=False)
    
class DFSerializer(serializers.Serializer):
    Timestamp = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Temperature = serializers.FloatField(required=False)
    Humidity = serializers.FloatField(required=False)
    Wind = serializers.FloatField(required=False)
    Wind_Direction = serializers.FloatField(required=False)

    