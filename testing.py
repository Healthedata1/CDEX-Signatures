'''
(venv37) ERICS-AIR-2:Venv ehaas$ openssl rsa -in jwt-key -pubout > jwt-key.pub
writing RSA key
(venv37) ERICS-AIR-2:Venv ehaas$ cat jwt-key.pub
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArHUXG64QmYaRhqWRe4Ny
Bvu9G0KPZHd0Lm70gnCJ8pdbgsHS8FzfxxS/qzcGGPNYPKOMNHMfvo2s/ctP472P
aTzUkfjWgJozETIH1hCXTBOb/0/wlkaQOlJHOTLtIJHJlfVaDONLn0bCshft/PUD
X/halBnYkV07vLSvwnYmflujfNW4r68iT/GIAnWHuzxyDWs0D3bcOT2vUDtDs5T6
BHndd6dNZ2/yJSV+1yjlICesavHLI5lNKz0mmhp4NTNXfHmAnM6UHDnUauuJlYZl
MChxoD/CsrJWXwhGvkP39CCHthHG/V9Me9IX4uhqeenVQ4AwkDDyNuVz4F9y5+Np
jj/J/Rc/wVEVlJlJqLYOfiXrQICNjT7R7l7DC3AHAtiSIYIDfLzQ9ROpVuX4Ypx6
J8HAuXU7XKXSk/l1M4G483nWW/OPqUSxKazjtPC7QMufpwz5iK2WVUmR+2yHQDI1
FcSqSh/xvFNVsHI+9LVfWrjmb0mrcv+ymOMQJ1r9kchGAieMMFlfblaQYkv8kmXr
Vy97mtb0F/unE4sEaiMFlyQm/XJVldMDvLaEDM6yex/VK18RTW59K3U8SDCWOUEG
/BUpO9YM9Jq4qi75EMzxEX+NHSBMLyVKJ46Xqry2Dvoji1X7Z50R7+JuZmoBqCpm
Gy1B0a5Z3xU9nCjxmYy1JT0CAwEAAQ==
-----END PUBLIC KEY-----
(venv37) ERICS-AIR-2:Venv ehaas$

#The MODULUS and the exponent are in the public key, and you can get them using the following command:

# exponent is almost always 65537

openssl rsa -pubin -in jwt-key.pub -text -noout
Public-Key: (4096 bit)
Modulus:
    00:ac:75:17:1b:ae:10:99:86:91:86:a5:91:7b:83:
    72:06:fb:bd:1b:42:8f:64:77:74:2e:6e:f4:82:70:
    89:f2:97:5b:82:c1:d2:f0:5c:df:c7:14:bf:ab:37:
    06:18:f3:58:3c:a3:8c:34:73:1f:be:8d:ac:fd:cb:
    4f:e3:bd:8f:69:3c:d4:91:f8:d6:80:9a:33:11:32:
    07:d6:10:97:4c:13:9b:ff:4f:f0:96:46:90:3a:52:
    47:39:32:ed:20:91:c9:95:f5:5a:0c:e3:4b:9f:46:
    c2:b2:17:ed:fc:f5:03:5f:f8:5a:94:19:d8:91:5d:
    3b:bc:b4:af:c2:76:26:7e:5b:a3:7c:d5:b8:af:af:
    22:4f:f1:88:02:75:87:bb:3c:72:0d:6b:34:0f:76:
    dc:39:3d:af:50:3b:43:b3:94:fa:04:79:dd:77:a7:
    4d:67:6f:f2:25:25:7e:d7:28:e5:20:27:ac:6a:f1:
    cb:23:99:4d:2b:3d:26:9a:1a:78:35:33:57:7c:79:
    80:9c:ce:94:1c:39:d4:6a:eb:89:95:86:65:30:28:
    71:a0:3f:c2:b2:b2:56:5f:08:46:be:43:f7:f4:20:
    87:b6:11:c6:fd:5f:4c:7b:d2:17:e2:e8:6a:79:e9:
    d5:43:80:30:90:30:f2:36:e5:73:e0:5f:72:e7:e3:
    69:8e:3f:c9:fd:17:3f:c1:51:15:94:99:49:a8:b6:
    0e:7e:25:eb:40:80:8d:8d:3e:d1:ee:5e:c3:0b:70:
    07:02:d8:92:21:82:03:7c:bc:d0:f5:13:a9:56:e5:
    f8:62:9c:7a:27:c1:c0:b9:75:3b:5c:a5:d2:93:f9:
    75:33:81:b8:f3:79:d6:5b:f3:8f:a9:44:b1:29:ac:
    e3:b4:f0:bb:40:cb:9f:a7:0c:f9:88:ad:96:55:49:
    91:fb:6c:87:40:32:35:15:c4:aa:4a:1f:f1:bc:53:
    55:b0:72:3e:f4:b5:5f:5a:b8:e6:6f:49:ab:72:ff:
    b2:98:e3:10:27:5a:fd:91:c8:46:02:27:8c:30:59:
    5f:6e:56:90:62:4b:fc:92:65:eb:57:2f:7b:9a:d6:
    f4:17:fb:a7:13:8b:04:6a:23:05:97:24:26:fd:72:
    55:95:d3:03:bc:b6:84:0c:ce:b2:7b:1f:d5:2b:5f:
    11:4d:6e:7d:2b:75:3c:48:30:96:39:41:06:fc:15:
    29:3b:d6:0c:f4:9a:b8:aa:2e:f9:10:cc:f1:11:7f:
    8d:1d:20:4c:2f:25:4a:27:8e:97:aa:bc:b6:0e:fa:
    23:8b:55:fb:67:9d:11:ef:e2:6e:66:6a:01:a8:2a:
    66:1b:2d:41:d1:ae:59:df:15:3d:9c:28:f1:99:8c:
    b5:25:3d
Exponent: 65537 (0x10001)

#to get just modulus in as string

openssl rsa -pubin -in jwt-key.pub -modulus -noout
Modulus=AC75171BAE1099869186A5917B837206FBBD1B428F6477742E6EF4827089F2975B82C1D2F05CDFC714BFAB370618F3583CA38C34731FBE8DACFDCB4FE3BD8F693CD491F8D6809A33113207D610974C139BFF4FF09646903A52473932ED2091C995F55A0CE34B9F46C2B217EDFCF5035FF85A9419D8915D3BBCB4AFC276267E5BA37CD5B8AFAF224FF188027587BB3C720D6B340F76DC393DAF503B43B394FA0479DD77A74D676FF225257ED728E52027AC6AF1CB23994D2B3D269A1A783533577C79809CCE941C39D46AEB89958665302871A03FC2B2B2565F0846BE43F7F42087B611C6FD5F4C7BD217E2E86A79E9D54380309030F236E573E05F72E7E3698E3FC9FD173FC15115949949A8B60E7E25EB40808D8D3ED1EE5EC30B700702D8922182037CBCD0F513A956E5F8629C7A27C1C0B9753B5CA5D293F9753381B8F379D65BF38FA944B129ACE3B4F0BB40CB9FA70CF988AD96554991FB6C8740323515C4AA4A1FF1BC5355B0723EF4B55F5AB8E66F49AB72FFB298E310275AFD91C84602278C30595F6E5690624BFC9265EB572F7B9AD6F417FBA7138B046A2305972426FD725595D303BCB6840CCEB27B1FD52B5F114D6E7D2B753C483096394106FC15293BD60CF49AB8AA2EF910CCF1117F8D1D204C2F254A278E97AABCB60EFA238B55FB679D11EFE26E666A01A82A661B2D41D1AE59DF153D9C28F1998CB5253D

'''
from jose import jwt
from json import dumps,loads
from base64 import urlsafe_b64encode as b64
my_r = '''
{
  "resourceType": "RelatedPerson",
  "id": "wouden-partner",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-relatedperson"
    ]
  },
  "active": true,
  "patient": {
    "reference": "Patient/example",
    "display": "Amy V. Shaw"
  },
  "relationship": [
    {
      "coding": [
        {
          "system": "http://hl7.org/fhir/v3/RoleCode",
          "code": "NIECE",
          "display": "niece"
        }
      ]
    }
  ],
  "name": [
    {
      "use": "official",
      "family": "van Putten",
      "given": [
        "Sarah"
      ]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "555-555-5555",
      "use": "home"
    },
    {
      "system": "email",
      "value": "sarah.vanputten@example.com",
      "use": "home"
    }
  ],
  "birthDate": "1996-01-28",
  "address": [
    {
      "use": "home",
      "line": [
        "80A Village Street"
      ],
      "city": "New Holland",
      "state": "PA",
      "postalCode": "17557"
    }
  ]
}
'''
private_key = open('jwt-key').read()
claims = '{"foo": "bar"}' # instead of this a hash of the claim in hexadecimal
key = 'secret'
headers = {
  #"alg": "HS256",
  #"alg": "RS256",
  #"typ": "JWT",
}

#print (loads(my_r))

#help(jws.sign)
token = jwt.encode(loads(claims), private_key, algorithm='RS256')
# u'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg'

#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
#help(jwt.decode)
#decode(token, key, algorithms=None, options=None, audience=None, issuer=None, subject=None, access_token=None)

public_key ='''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArHUXG64QmYaRhqWRe4Ny
Bvu9G0KPZHd0Lm70gnCJ8pdbgsHS8FzfxxS/qzcGGPNYPKOMNHMfvo2s/ctP472P
aTzUkfjWgJozETIH1hCXTBOb/0/wlkaQOlJHOTLtIJHJlfVaDONLn0bCshft/PUD
X/halBnYkV07vLSvwnYmflujfNW4r68iT/GIAnWHuzxyDWs0D3bcOT2vUDtDs5T6
BHndd6dNZ2/yJSV+1yjlICesavHLI5lNKz0mmhp4NTNXfHmAnM6UHDnUauuJlYZl
MChxoD/CsrJWXwhGvkP39CCHthHG/V9Me9IX4uhqeenVQ4AwkDDyNuVz4F9y5+Np
jj/J/Rc/wVEVlJlJqLYOfiXrQICNjT7R7l7DC3AHAtiSIYIDfLzQ9ROpVuX4Ypx6
J8HAuXU7XKXSk/l1M4G483nWW/OPqUSxKazjtPC7QMufpwz5iK2WVUmR+2yHQDI1
FcSqSh/xvFNVsHI+9LVfWrjmb0mrcv+ymOMQJ1r9kchGAieMMFlfblaQYkv8kmXr
Vy97mtb0F/unE4sEaiMFlyQm/XJVldMDvLaEDM6yex/VK18RTW59K3U8SDCWOUEG
/BUpO9YM9Jq4qi75EMzxEX+NHSBMLyVKJ46Xqry2Dvoji1X7Z50R7+JuZmoBqCpm
Gy1B0a5Z3xU9nCjxmYy1JT0CAwEAAQ==
-----END PUBLIC KEY-----
'''
Modulus="AC75171BAE1099869186A5917B837206FBBD1B428F6477742E6EF4827089F2975B82C1D2F05CDFC714BFAB370618F3583CA38C34731FBE8DACFDCB4FE3BD8F693CD491F8D6809A33113207D610974C139BFF4FF09646903A52473932ED2091C995F55A0CE34B9F46C2B217EDFCF5035FF85A9419D8915D3BBCB4AFC276267E5BA37CD5B8AFAF224FF188027587BB3C720D6B340F76DC393DAF503B43B394FA0479DD77A74D676FF225257ED728E52027AC6AF1CB23994D2B3D269A1A783533577C79809CCE941C39D46AEB89958665302871A03FC2B2B2565F0846BE43F7F42087B611C6FD5F4C7BD217E2E86A79E9D54380309030F236E573E05F72E7E3698E3FC9FD173FC15115949949A8B60E7E25EB40808D8D3ED1EE5EC30B700702D8922182037CBCD0F513A956E5F8629C7A27C1C0B9753B5CA5D293F9753381B8F379D65BF38FA944B129ACE3B4F0BB40CB9FA70CF988AD96554991FB6C8740323515C4AA4A1FF1BC5355B0723EF4B55F5AB8E66F49AB72FFB298E310275AFD91C84602278C30595F6E5690624BFC9265EB572F7B9AD6F417FBA7138B046A2305972426FD725595D303BCB6840CCEB27B1FD52B5F114D6E7D2B753C483096394106FC15293BD60CF49AB8AA2EF910CCF1117F8D1D204C2F254A278E97AABCB60EFA238B55FB679D11EFE26E666A01A82A661B2D41D1AE59DF153D9C28F1998CB5253D"

Modulus_int = int(Modulus, 16)

# construct jwk
from jose import jwk

#print(help(jwk))

exp = 'AQAB' # usually this
mod ='AKx1FxuuEJmGkYalkXuDcgb7vRtCj2R3dC5u9IJwifKXW4LB0vBc38cUv6s3BhjzWDyjjDRzH76NrP3LT-O9j2k81JH41oCaMxEyB9YQl0wTm_9P8JZGkDpSRzky7SCRyZX1WgzjS59GwrIX7fz1A1_4WpQZ2JFdO7y0r8J2Jn5bo3zVuK-vIk_xiAJ1h7s8cg1rNA923Dk9r1A7Q7OU-gR53XenTWdv8iUlftco5SAnrGrxyyOZTSs9JpoaeDUzV3x5gJzOlBw51GrriZWGZTAocaA_wrKyVl8IRr5D9_Qgh7YRxv1fTHvSF-Loannp1UOAMJAw8jblc-BfcufjaY4_yf0XP8FRFZSZSai2Dn4l60CAjY0-0e5ewwtwBwLYkiGCA3y80PUTqVbl-GKceifBwLl1O1yl0pP5dTOBuPN51lvzj6lEsSms47Twu0DLn6cM-YitllVJkftsh0AyNRXEqkof8bxTVbByPvS1X1q45m9Jq3L_spjjECda_ZHIRgInjDBZX25WkGJL_JJl61cve5rW9Bf7pxOLBGojBZckJv1yVZXTA7y2hAzOsnsf1StfEU1ufSt1PEgwljlBBvwVKTvWDPSauKou-RDM8RF_jR0gTC8lSieOl6q8tg76I4tV-2edEe_ibmZqAagqZhstQdGuWd8VPZwo8ZmMtSU9'
my_jwk_public = {
    "kid": "my_key",
    "use": "sig",
    "alg": "RS256",
    "kty": "RSA",
    "n": mod,
    "e": exp,
}

# my_key = {
#     "kty": "oct",
#     "kid": "018c0ae5-4d9b-471b-bfd6-eef314bc7037",
#     "use": "sig",
#     "alg": "HS256",
#     "k": "hJtXIZ2uSN5kbQfbtTNWbpdmhkV8FJG-Onbc6mxCcYg"
# }
#
# my_key = {
#     "kty": "RSA",
#     "e": "AQAB",
#     "use": "sig",
#     "kid": "_Y9xUzo2cCSdmIwi5U__LH_wJCMaYCzq4zMyQFymi6Q",
#     "alg": "RS256",
#     "n": "oC-MDpYr67lOPFivUwHVVNJYqo4EdyuUKgwzhAAsK69gwBypoCcJdekt7TyXPHl1NQ-n8Q5jvf8cE4x81Xcf-u8kW-Rdq_HwyngECgbSGw5D8WcnaGssmrMV9KzMqEJryLwxNCnGvrPuKHQrjzkJvB7kbwD3BTNjunKI69UiN-d6z5rocVFXFcugdcWw9qDpK1OztogrWmOkU0lM73CCHlGOFLH7FXyqp-h7rGheFvaevtOhCF-kgFe-c0hViZeHVR3Vhob3eLwRIJ-t7JRqaaMb_2hs--SxncgqyEE_GYBy6PT9Ds5xcrfRpzzDDp0qe2uD5XGlyzHR3AYfNav9zQ"
# }

print(my_jwk_public)
my_key = jwk.construct(my_jwk_public)
print(f'my_jwk = {my_key}')
#print(help(my_key))

# unencoded_claim = jwt.decode(token, public_key, algorithms=['RS256'])
# # {u'key': u'value'}
# unencoded_header = jwt.get_unverified_header(token)
# print(token)
# print(unencoded_claim)
# print(unencoded_header)

#then compare hash of canonicalization with hash in the signature to verify.

#use JWS to do all of this
from jose import jws
import hashlib

# private_key = '''-----BEGIN PRIVATE KEY-----
# MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCzuFi1bCJhC1sD
# JNe74AYTGq6ECa9+zrkBtiXbvBbFM0mY56gvUtAOSRK7l5rQTZ/oEeDhOD4ELV1l
# kLPi+7wh4zg/gt2LA67C0nkKeAK6qibDHgXRwArf8trnddbo+9PbT/0/1nPTzkyK
# 6BQA6ENBDKlS3yzh+iCZVVwJY04nby+NR2iduIPZnIp9m62Kbzv1xhyib6cU84L/
# 8BGhUPhXg75DcEqJrsuLXOfakRWH9e0Q0BwuGIcvndCFN0T8PZguz0+LhcF28tOu
# ej/PDxDbdOvmWOT0IiQtZ7jxdSevLxJMGA2XV1luBWoh73pXJ2hYPuIFBylmwhVN
# KS5lM/lDAgMBAAECggEAOyw1OPazkxQ0ESLuTRODrIKadyrhN3VFAMVCTcjuDlvG
# nauYeoxfqHRy0IUoGfGU9sn8Kutjr+hn2er8731HAjlX6cFixESgI9E8vS+qZl9j
# h9a4v8jlS7sgTBlGe0t/A7Sgg4ZOeKxyE0I6Y9oVWrOahIiqtHSwiwvJ0+V4dA7g
# Z/xvO2SdRmzGkaMHq2v7TeV+xg5cTM34Lram7uFfBCuw/uBuTeLUt4TDwAQcBPnV
# YWVe/Wylbd0sox25ekSIsuDZj9uetlkMDGQSY+a4GAUhVECngukR+QGqiIyFi6AH
# m1v+LgatTnhUWkZKTQGsL0JNOZbAMObiTgxw8hg+gQKBgQDbDK6OeG75nSsy3iC4
# GvlqR+NrJTDfhvvFalBq8jhCNK/aCg6Ykm1fsCVkjWFtuVjDkuV3PpgZHk8NsjHR
# 6my2cmfonnw4fr3i+HhQOnxBX1UV3XgpRawtq5aeuCcPLizNquDERN8Z7DPgAOTA
# c1rTjg+eQnto08JltWTA8MzhIQKBgQDSCUiK5YhEv6IvqQwiUrrbyewhCg6DRpE/
# iK6alpsS2KVe/EPzPMnZc4IrYWdqYvBGzg93IZ6HzmlgtMOS6ZjZS7nBmv74KKNj
# iWvlMBi0+Njlv/ZaHh4EVuvNP4Jd+jdC88swDT7PkbJgB1ZE0yqNnOf06dz/xAH/
# NmcqTGg54wKBgG8MFtITK+9PRj8bbOrogdjnaNtAl246OBj0tKAC+5JUs3GN96hR
# UzFXUx2Orv25IM7FAZ9aFDFntBv1YlxQw5wak6LR9ZeOaSVPYW8Kt0NM2Q2koO4L
# bCYa/tin8uU3O29oWVomsBOsMwA0c8M8t6bYNgK9IWMbN0nok5NcgAEBAoGBAIBE
# iRfB+0k42rxOeYmQimrlUp4OvTQwaU2qlC72ILgOtFdgqcKm8gIpR2pkrrpKt8AV
# 4V34mw8G4FXdrr5OiDjTxRpWJLW6Y6XK66hoif4jJpqQc8svL1epGZIb4eqwfwUV
# S5YJ0L0EljGM6YNYjlkzZHiuRXew5SNNvw0W4mPPAoGBAMmzlWmmbCe8n9m4awD1
# ifKVcYWgfW09FNYQf+91JV/9opB3Hk8yfP0b+7P91q90n1j627ys8QKUWQZ+MnQG
# xjgzBRtLVsiIcs5E9ZL1jAk+tOBwmaT+fcRUWX94ZLO2f7Gu0frLGpYy1BL3kCIE
# 4mvM0sggFYS/97zk0KWngpEL
# -----END PRIVATE KEY-----'''
#
# my_jwk_public = {
#     "kty": "RSA",
#     "e": "AQAB",
#     "use": "sig",
#     "kid": "jDiIDNLbYQ91ykdRZqDp5xwiRtihITkd8WBWCAhCtkw",
#     "alg": "RS256",
#     "n": "s7hYtWwiYQtbAyTXu-AGExquhAmvfs65AbYl27wWxTNJmOeoL1LQDkkSu5ea0E2f6BHg4Tg-BC1dZZCz4vu8IeM4P4LdiwOuwtJ5CngCuqomwx4F0cAK3_La53XW6PvT20_9P9Zz085MiugUAOhDQQypUt8s4fogmVVcCWNOJ28vjUdonbiD2ZyKfZutim879cYcom-nFPOC__ARoVD4V4O-Q3BKia7Li1zn2pEVh_XtENAcLhiHL53QhTdE_D2YLs9Pi4XBdvLTrno_zw8Q23Tr5ljk9CIkLWe48XUnry8STBgNl1dZbgVqIe96VydoWD7iBQcpZsIVTSkuZTP5Qw"
# }

print(f'claim = {claims}')
print(f'claim.encode() = {claims.encode()}')
print(f'hashlib.sha256.claim = {hashlib.sha256(claims.encode())}')

print(f"The binary equivalent of SHA256 is :\n {hashlib.sha256(claims.encode()).digest()}")
payload =  hashlib.sha256(claims.encode()).digest()
#print(type(payload), type(private_key))
help(jws.sign)
# help(jws.verify)
# help(jws)

#finally use the header to convey the hash and public key
my_header = {'jwk': my_jwk_public, 'hash': 'sha256'}

my_signature = jws.sign(payload, private_key, algorithm='RS256', headers=my_header)

print(f'my_signature = {my_signature}' )
#get claims, headers
print(f'jws.get_unverified_claims(my_signature)={jws.get_unverified_claims(my_signature)}')
print(f'jws.get_unverified_header(my_signature)={jws.get_unverified_header(my_signature)}')
#verify sig with public key and that hash from claim is the same has from object
#get public_key from the header (JWT)
jwk_public = jws.get_unverified_header(my_signature)['jwk']
print(f'jwk_public ={jwk_public}' )

try:
    verify = jws.verify(my_signature, jwk_public , algorithms=['RS256'])
    assert(jws.get_unverified_claims(my_signature) == hashlib.sha256(claims.encode()).digest())
    print(f'verified!!!')

except:
    print("whoops not verified!!!")



# can also use detached web signatures see  https://medium.com/gin-and-tonic/implementing-detached-json-web-signature-9ca5665ddcfc

# create JWS as above and remove the payload

split_sig = my_signature.split('.')
print( f'split_sig[1] = {split_sig[1]}')
split_sig[1] = ''
my_signature = '.'.join(split_sig)
print(f'my_signature = {my_signature}')

# check if can verify
try:
    verify = jws.verify(my_signature, jwk_public , algorithms=['RS256'])
    assert(jws.get_unverified_claims(my_signature) == hashlib.sha256(claims.encode()).digest())
    print(f'verified!!!')

except:
    print("whoops not verified!!!")

#rehash the content and add it back in as base64_url

payload =  hashlib.sha256(claims.encode()).digest()  # binary
payload  = b64(payload).replace(b'=', b'')

print(f'payload = {payload.decode()}' )

split_sig[1] = payload.decode()
my_signature = '.'.join(split_sig)

try:
    verify = jws.verify(my_signature, jwk_public , algorithms=['RS256'])
    assert(jws.get_unverified_claims(my_signature) == hashlib.sha256(claims.encode()).digest())
    print(f'verified!!!')

except:
    print("whoops not verified!!!")

# OK no hashing this time using minimize resource as claim

#canonicalize resources

payload = dumps(my_r, sort_keys=True,separators=(',', ':'))

# use the header to convey  public key no hash needed this time.
my_header = {'jwk': my_jwk_public,}

my_signature = jws.sign(payload.encode(), private_key, algorithm='RS256', headers=my_header)

print(f'my_signature = {my_signature}' )
#get claims, headers
print(f'jws.get_unverified_claims(my_signature)={jws.get_unverified_claims(my_signature)}')
print(f'jws.get_unverified_header(my_signature)={jws.get_unverified_header(my_signature)}')

#remove payload

split_sig = my_signature.split('.')
split_sig[1] = ''
my_signature = '.'.join(split_sig)
print(f'my_signature = {my_signature}')

# check if can verify
print(f'jws.get_unverified_claims(my_signature)={jws.get_unverified_claims(my_signature)}')
print(f'jws.get_unverified_header(my_signature)={jws.get_unverified_header(my_signature)}')
try:
    verify = jws.verify(my_signature, jwk_public , algorithms=['RS256'])
    assert(jws.get_unverified_claims(my_signature) ==  dumps(my_r, sort_keys=True,separators=(',', ':')).encode())
    print(f'verified!!!')

except:
    print("whoops not verified!!!")

# add payload back in...
# pop off signature element
# canonicalize resources

payload = dumps(my_r, sort_keys=True,separators=(',', ':'))
#base64_url encode it
payload  = b64(payload.encode()).replace(b'=', b'')

print(f'payload = {payload.decode()}' )

split_sig[1] = payload.decode()
#split_sig[1] = 'abcd'
my_signature = '.'.join(split_sig)

print(f'jws.get_unverified_claims(my_signature)={jws.get_unverified_claims(my_signature)}')
print(f'jws.get_unverified_header(my_signature)={jws.get_unverified_header(my_signature)}')
jwk_public = jws.get_unverified_header(my_signature)['jwk']
print(f'jwk_public ={jwk_public}' )
try:
    verify = jws.verify(my_signature, jwk_public , algorithms=['RS256'])
    assert(jws.get_unverified_claims(my_signature) ==  dumps(my_r, sort_keys=True,separators=(',', ':')).encode())
    print(f'verified!!!')

except:
    print("whoops not verified!!!")


my_signature = jws.sign(b'abcde', private_key, algorithm='RS256', headers=my_header)

print(f'my_signature = {my_signature}' )
labels = ['header', 'payload', 'signature']
for i,j in enumerate(my_signature.split('.')):
    print(f'{labels[i]}: {j}')
    print('='*80)
print(f'jws.get_unverified_claims(my_signature)={jws.get_unverified_claims(my_signature)}')
print(f'jws.get_unverified_header(my_signature)={jws.get_unverified_header(my_signature)}')

# remove payload

# recreate payload

# validate in the usual manner....
