from api_helper import StarApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = StarApiPy()

#credentials
uid   = "T0009"
pwd     = "Qwe@1234"
factor2 = "24101996"
vc      = "T0009"
app_key = "pssUATMKTMKRAPI0912GDL901A"
imei    = "xyz12345"
#make the api call
ret = api.login(userid=uid, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

print(ret)

