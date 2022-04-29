from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import UserAccount, Transactions
from django.http.response import JsonResponse
from typing import Optional


class AddMoneyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        account = UserAccount.objects.get(user=request.user)
        data = request.data
        log_transaction = account.balance
        account.add_money(data.get('value'))
        account.save()
        transaction = Transactions.objects.create(
            value = data.get('value'),
            description = data.get('description'),
            account = account,
            type = 'CREDIT',
            log_extract = log_transaction
        )
        return Response({'msg': 'OK'})


class RemoveMoneyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        account = UserAccount.objects.get(user=request.user)
        data = request.data
        log_transaction = account.balance
        remove_money = account.remove_money(data.get('value'))
        if remove_money == True:
            account.save()
            transaction = Transactions.objects.create(
                value = data.get('value'),
                description = data.get('description'),
                account = account,
                type = 'DEBIT',
                log_extract = log_transaction
            )
            return Response({'msg': 'OK'})
        return Response({'msg': 'Error'})


class ExtractView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def response_object(self, data):
        data_format = [
            {
                'Date': transaction.datetime,
                'Value': transaction.value,
                'Type': transaction.type,
                'Description': transaction.description,
            }
            for transaction in data
        ]
        initial_balance = data[0].log_extract
        final_balance = data[len(data_format)-1].log_extract
        payload = {
            "Initial_balance": initial_balance,
            "Final_balance": final_balance,
            "Extract": data_format
        }
        return JsonResponse(payload, safe=False)

    def get(self, request, initial=None, final=None, type=None):
        account = UserAccount.objects.get(user=request.user)

        if type==None and initial==None and final==None:
            data = Transactions.objects.filter(account=account)
            return self.response_object(data)

        elif type and initial==None and final==None:
            data = Transactions.objects.filter(account=account, type=type)
            return self.response_object(data)

        elif type==None and initial and final:
            data = Transactions.objects.filter(account=account, datetime__range=[initial, final])
            return self.response_object(data)

        elif type and initial and final:
            data = Transactions.objects.filter(account=account, datetime__range=[initial, final], type=type)
            return self.response_object(data)
            
