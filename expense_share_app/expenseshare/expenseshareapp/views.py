from django.shortcuts import render
from expenseshareapp.models import *
from rest_framework.views import APIView
from expenseshareapp.serializers import *
from rest_framework.response import Response
import json
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.

class Amountandparticipants(APIView):
    def post(self, request):
        serializer = AmountandparticipantSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("success")
        else:
            return Response("Not success")
        
class expensecalculation(APIView):
    def post(self, request):
        total_amount = request.data.get('total_amount')
        total_participants = request.data.get('total_participants')
        first_installment_receiver = request.data.get('first_installment_receiver')
        each_participater_owe = total_amount/len(total_participants)
        data = []
        for i in total_participants:
            # return Response(first_installment_receiver)
            Participantowe.objects.create(user_id = i,first_installment = each_participater_owe,total = each_participater_owe,first_installment_receiver_id = first_installment_receiver)
            payable_installment = Participantowe.objects.filter(user_id = i).first()
            data.append({i:f"User-{i} owes User-{payable_installment.first_installment_receiver_id}: Rs {payable_installment.total}"})
            email = User.objects.filter(id = i).first()
            receiver = User.objects.filter(id = payable_installment.first_installment_receiver_id).first()
            datas = f"User-{email.first_name} owes User-{receiver.first_name}: Rs {payable_installment.total}"
            from_email = 'ganshyamnagar11@gmail.com'
            email = User.objects.filter(id = i).first()
            to = [email.email]
            plaintext = get_template('expenseshareapp/expense.html')
            htmly = get_template('expenseshareapp/expense.html')
            d = {'data': datas}
            subject, from_email, to = 'Expense Share Application', from_email, to
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(
                subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        return Response(data)
    
class userregister(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        serializer = UserregisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # return Response(serializer.data)
            id = serializer.data['id']
            UserProfile.objects.create(user_id = id,phone_number = phone_number)
            return Response("success")
        else:
            return Response("Not success")
        
class flipcartsaleowe(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        amount = request.data.get('amount')
        second_installment_receiver = request.data.get('second_installment_receiver')
        try:
            f_installment = Participantowe.objects.filter(user_id = user_id).first()
            total = int(f_installment.first_installment) + int(amount)
            Participantowe.objects.filter(user_id = user_id).update(second_installment = amount,total = total,second_installment_receiver_id = second_installment_receiver)
        except:
            Participantowe.objects.create(user_id = user_id, second_installment = amount,total =  amount,second_installment_receiver_id= second_installment_receiver)
        payable_installment = Participantowe.objects.filter(user_id = user_id).first()
        email = User.objects.filter(id = user_id).first() 
        reciever = User.objects.filter(id = second_installment_receiver).first() 
        res = f"User-{user_id} owes User-{payable_installment.second_installment_receiver_id}: {payable_installment.total} ({payable_installment.first_installment} + {payable_installment.second_installment})"
        email_data = f"User-{email.first_name} owes User-{reciever.first_name}: {payable_installment.total} ({payable_installment.first_installment} + {payable_installment.second_installment})"
        from_email = 'ganshyamnagar11@gmail.com'
        
        to = [email.email]
        plaintext = get_template('expenseshareapp/expense.html')
        htmly = get_template('expenseshareapp/expense.html')
        d = {'data': email_data}
        subject, from_email, to = 'Expense Share Application', from_email, to
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response(res)
    
# class flipcartsaleowe(APIView):
#     def get(self, request):
#         payable_installment = Participantowe.objects.all().values()
#         data = []
#         for i in payable_installment:
#             data.append({})
#         res = f"User-{user_id} owes User {payable_installment.second_installment_receiver}: {payable_installment.total} ({payable_installment.first_installment} + {payable_installment.second_installment})"
#         return Response(res)
    
class thirdinstallmentowe(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        amount = request.data.get('amount')
        third_installment_receiver = request.data.get('third_installment_receiver')
        try:
            f_installment = Participantowe.objects.filter(user_id = eval(user_id)).first()
            if f_installment.first_installment == None:
                f_installment.first_installment = 0
            if f_installment.second_installment == None:
                f_installment.second_installment = 0
            if eval(user_id) == f_installment.first_installment_receiver_id:
                total =  int(f_installment.second_installment) + int(amount) - int(f_installment.first_installment)
                # return Response(total)
            if eval(user_id) == f_installment.second_installment_receiver_id:
                total =  int(f_installment.first_installment) + int(amount) - int(f_installment.second_installment)
            Participantowe.objects.filter(user_id = eval(user_id)).update(third_installment = amount,total = total,third_installment_receiver_id = third_installment_receiver)
        except:
            if f_installment.first_installment == None:
                f_installment.first_installment = 0
            if f_installment.second_installment == None:
                f_installment.second_installment = 0
            Participantowe.objects.create(user_id = eval(user_id), third_installment = amount,total =  amount,third_installment_receiver_id = third_installment_receiver)
            payable_installment = Participantowe.objects.filter(user_id = eval(user_id)).first()
            res = f"User-{user_id} owes User ({payable_installment.third_installment_receiver_id}: {abs(amount)} ({payable_installment.first_installment} + {payable_installment.second_installment} + {payable_installment.third_installment})"
            email = User.objects.filter(id = eval(user_id)).first() 
            receiver = User.objects.filter(id = third_installment_receiver).first() 
            email_data = f"User-{email.first_name} owes User-{receiver.first_name}: {abs(amount)} ({payable_installment.first_installment} + {payable_installment.second_installment} + {payable_installment.third_installment})"
            from_email = 'ganshyamnagar11@gmail.com'
    
            to = [email.email]
        payable_installment = Participantowe.objects.filter(user_id = eval(user_id)).first()
        # 
        if eval(user_id) == payable_installment.first_installment_receiver_id:
                
                
                res = f"User-{user_id} owes User-{payable_installment.third_installment_receiver_id}: {abs(payable_installment.total)} ({payable_installment.first_installment} - {int(amount)})"
                email = User.objects.filter(id = eval(user_id)).first() 
                receiver = User.objects.filter(id = third_installment_receiver).first() 
                email_data = f"User-{email.first_name} owes User-{receiver.first_name}: {abs(payable_installment.total)} ({payable_installment.first_installment} - {int(amount)})"
                from_email = 'ganshyamnagar11@gmail.com'
        
                to = [email.email]
        if eval(user_id) == payable_installment.second_installment_receiver_id:
                res = f"User-{user_id} owes User ({payable_installment.third_installment_receiver_id}: abs({payable_installment.total}) ({payable_installment.second_installment} - {int(amount)})"
                email = User.objects.filter(id = eval(user_id)).first() 
                receiver = User.objects.filter(id = third_installment_receiver).first() 
                email_data = f"User-{email.first_name} owes User-{receiver.first_name}: {abs(payable_installment.total)} ({payable_installment.second_installment} - {int(amount)})"
                from_email = 'ganshyamnagar11@gmail.com'
        
                to = [email.email]
        
        plaintext = get_template('expenseshareapp/expense.html')
        htmly = get_template('expenseshareapp/expense.html')
        d = {'data': email_data}
        subject, from_email, to = 'Expense Share Application', from_email, to
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response(res)
    
    
        