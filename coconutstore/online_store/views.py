import logging
from django.shortcuts import render
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# Create your views here.
import json
from online_store import common
from online_store.models import Customer,DeliveryPartner


@api_view(['GET', 'POST'])
def mobile_auth(request):
    if request.method == 'POST':
        mobile_number = request.data.get('mobile')
        isValidNumber = common.isValidMobileNumber(mobile_number)
        password = request.data.get('password')
        if password is None or len(password)<4:
            return Response({"message":"Please provide password greated than 4 letters."},status=status.HTTP_206_PARTIAL_CONTENT)
        if isValidNumber["isValid"]:
            _user,created = User.objects.get_or_create(
                        username=f'{mobile_number}',
                        password=f'{password}   ',
                    )
            if created:
                logging.info(f'User successfully created with username : {mobile_number}')
            _customer,created = Customer.objects.get_or_create(
                            User = _user,
                            MobileNumber = mobile_number
                        )
            if created:
                logging.info(f'Customer successfully created with username : {mobile_number}')
            if not _customer.IsVerified:
                otpResponse = common.send_otp(mobile_number,_customer)
                if otpResponse['return'] == False:
                    return Response(otpResponse,status=status.HTTP_412_PRECONDITION_FAILED)
                else:
                    return Response(otpResponse)
            return Response({"message": f'Customer Mobile number {mobile_number} is already Verified. Please login with password.'},status=status.HTTP_200_OK)
        else:
            return Response(isValidNumber)
    return Response({"message": "Hello, world!"})


@api_view(['POST'])
def verifyOtp(request):
    try:
        if request.method == 'POST':
            mobile_number = request.data.get('mobile')
            otp = request.data.get('otp')
            _user = User.objects.filter(username=mobile_number).first()
            print(_user)
            if _user is not None:
                _customer = Customer.objects.filter(User=_user).first()
                print(otp,_customer.Otp)
                if str(otp).strip() == str(_customer.Otp).strip():
                    _customer.IsVerified = True
                    _customer.save()
                    return Response({"message":"User verified successfully"},status = status.HTTP_202_ACCEPTED)
                else:
                     return Response({"message":"Incorrect OTP. Please re-enter the OTP."},status = status.HTTP_417_EXPECTATION_FAILED)
                    
    except Exception as e:
        print(e)
        return Response({"message":"Something went wrong.","exception":e.__cause__},status = status.HTTP_424_FAILED_DEPENDENCY)