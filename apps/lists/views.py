from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
from .models import List, ListItem


class ListSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(
    #     queryset=get_user_model().objects.all())
    user = serializers.HyperlinkedRelatedField(
        queryset=get_user_model().objects.all(), view_name='user-detail')

    class Meta:
        model = List
        fields = ['name', 'description', 'user',
                  'created_at', 'updated_at', 'url']


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    # parent_list = serializers.PrimaryKeyRelatedField(
    #     queryset=List.objects.all())
    parent_list = serializers.HyperlinkedRelatedField(
        queryset=List.objects.all(), view_name='list-detail')

    class Meta:
        model = ListItem
        # fields = '__all__'
        # fields = ['text', 'parent_list', 'created_at', 'updated_at', 'url']
        fields = ['text', 'parent_list', 'created_at', 'updated_at']
        # read_only_fields = ['parent_list']
        # extra_kwargs = {
        #     'url': {'view_name': 'listitem-detail'},
        # }


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
