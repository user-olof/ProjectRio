from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from apps.users.models import CustomUser


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # lookup_field = 'id'

    # the method allows us to manage an instance when it's being created
    # Here we associate the User in the incoming request with the instance
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return super(AccountViewSet, self).get_queryset()
    
    def list(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        data = AccountSerializer(query_set, many=True, context={'request': request}).data
        return Response(data={'error': False, 'message': None, 'results': data})

    def retrieve(self, request, pk=None):
        query_set = self.get_queryset()
        data = AccountSerializer(query_set, many=True, context={'request': request}).data
        return Response(data)   

    def create(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        request_data = request.data
        account, created = Account.objects.get_or_create(
            name=request_data['name'],
            owner = request_data['owner']
        )
        data = AccountSerializer(account).data
        return Response(data={'error': False, 'message': "Account object successfully created", 'results': data})