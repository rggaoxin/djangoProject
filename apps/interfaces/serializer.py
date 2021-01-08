from rest_framework import serializers

from interfaces.models import Interfaces


class InterfaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        exclude = ('update_time', 'is_delete')
        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }
