from rest_framework.viewsets import GenericViewSet


class ListSerializerClass(GenericViewSet):
    list_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'list' and self.list_serializer_class:
            return self.list_serializer_class
        return self.serializer_class


class FileViewSetMixin(GenericViewSet):
    pass
