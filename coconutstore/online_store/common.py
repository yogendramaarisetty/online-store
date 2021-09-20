
import requests,json,logging, random, urllib
from rest_framework.response import Response
from rest_framework import status
import coconutstore.settings as settings
from online_store.models import Customer

def isValidMobileNumber(mobile_number):
    response = {"message":"","isValid":False}
    if len(mobile_number) is 10:
        headers = {'Content-Type': 'application/json;',
                'Authorization': f'Bearer {settings.TELNYX_AUTH_KEY}'}
        r = requests.get(f'https://api.telnyx.com/v2/number_lookup/+91{mobile_number}?type=carrier&type=caller-name',headers=headers)
        responseData = json.loads(r.text)
        if r.status_code is status.HTTP_200_OK:
            if isIndianNumberNotFraud(responseData):
                response["message"] = "Mobile number is Valid."
                response["isValid"] = True
            else:
                response["message"] = "Mobile number is not Indian number or it is a Fraud number."
        else:
            logging.error(f'Mobile Verfification API Failed.')
            response["message"] = "Mobile verification API failed."
    else:
        response["message"] = f'{mobile_number} is not a valid mobile number.\nPlease provide a valid Indian number.'
    
    return response

def isIndianNumberNotFraud(apiResponse):
    try:
        print(apiResponse["data"]["country_code"],apiResponse["data"]["fraud"])
        return apiResponse["data"]["country_code"] == "IN" and apiResponse["data"]["fraud"] == None
    except:
        return False

def send_otp(mobile_number,_customer):
    fourDigitOtp = random.randint(1111,9999)
    _customer.Otp = fourDigitOtp
    _customer.save()
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {"authorization": settings.FAST_TO_SMS_AUTH_KEY,
                   "variables_values": fourDigitOtp, "route": "otp", "numbers": mobile_number}
    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_dict = json.loads(response.text)
    print(response.text)   
    return  response_dict
