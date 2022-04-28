from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import UserAccount, Transactions
from django.http.response import JsonResponse


class AddMoneyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        account = UserAccount.objects.get(user=request.user)
        data = request.data
        account.add_money(data.get('value'))
        account.save()
        transaction = Transactions.objects.create(
            value = data.get('value'),
            description = data.get('description'),
            account = account,
            type = 'CREDIT'
        )
        return Response({'msg': 'OK'})


class RemoveMoneyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        account = UserAccount.objects.get(user=request.user)
        data = request.data
        remove_money = account.remove_money(data.get('value'))
        if remove_money == True:
            account.save()
            transaction = Transactions.objects.create(
                value = data.get('value'),
                description = data.get('description'),
                account = account,
                type = 'CREDIT'
            )
            return Response({'msg': 'OK'})
        return Response({'msg': 'Error'})


class ExtractView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        account = UserAccount.objects.get(user=request.user)
        data = Transactions.objects.filter(account=account)
        list_transaction = []
        for transaction in data:
            list_transaction.append(
                {
                    'Date': transaction.datetime,
                    'Value': transaction.value,
                    'Type': transaction.type,
                    'Description': transaction.description,
                }
            )
        
        return JsonResponse(list_transaction, safe=False)
