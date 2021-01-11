from rest_framework import serializers

from envs.models import Envs


# from projects.models import Projects


class EnvsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        exclude = ('update_time', 'is_delete')
        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }


class EnvNameserializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        exclude = ('id', 'name')
