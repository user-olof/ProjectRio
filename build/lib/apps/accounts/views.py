from rioacademy.apps.accounts.models import Account
from rioacademy.apps.accounts.serializers import AccountSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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