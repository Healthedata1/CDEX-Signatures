from base64 import urlsafe_b64encode as b64
import codecs as c

my_num = 65537
#my_num = 6

print(hex(my_num), type(hex(my_num)))

my_hex = hex(my_num)

print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(my_num))

bits = [1,0,1]

# 00000001 0000000 00000001
bits=['000000','010000','000000','000001']

for i in bits:
    print(int(i,2))
    #print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i))

a = c.decode('010001', 'hex')
b = b64(a)
d = b.decode()
print(a,b,d)

Modulus='00AC75171BAE1099869186A5917B837206FBBD1B428F6477742E6EF4827089F2975B82C1D2F05CDFC714BFAB370618F3583CA38C34731FBE8DACFDCB4FE3BD8F693CD491F8D6809A33113207D610974C139BFF4FF09646903A52473932ED2091C995F55A0CE34B9F46C2B217EDFCF5035FF85A9419D8915D3BBCB4AFC276267E5BA37CD5B8AFAF224FF188027587BB3C720D6B340F76DC393DAF503B43B394FA0479DD77A74D676FF225257ED728E52027AC6AF1CB23994D2B3D269A1A783533577C79809CCE941C39D46AEB89958665302871A03FC2B2B2565F0846BE43F7F42087B611C6FD5F4C7BD217E2E86A79E9D54380309030F236E573E05F72E7E3698E3FC9FD173FC15115949949A8B60E7E25EB40808D8D3ED1EE5EC30B700702D8922182037CBCD0F513A956E5F8629C7A27C1C0B9753B5CA5D293F9753381B8F379D65BF38FA944B129ACE3B4F0BB40CB9FA70CF988AD96554991FB6C8740323515C4AA4A1FF1BC5355B0723EF4B55F5AB8E66F49AB72FFB298E310275AFD91C84602278C30595F6E5690624BFC9265EB572F7B9AD6F417FBA7138B046A2305972426FD725595D303BCB6840CCEB27B1FD52B5F114D6E7D2B753C483096394106FC15293BD60CF49AB8AA2EF910CCF1117F8D1D204C2F254A278E97AABCB60EFA238B55FB679D11EFE26E666A01A82A661B2D41D1AE59DF153D9C28F1998CB5253D'

#convert to hex array

my_array = [Modulus[i:i+2] for i in range(0, len(Modulus), 2)]
print(my_array)

#convert to hex to bits
bit_string = ''
for i in my_array:
    mybyte = bytes.fromhex(i) # create my byte using a hex string
    binary_string = "{:08b}".format(int(mybyte.hex(),16))
    bit_string = bit_string + binary_string
print(bit_string)

#create 6 bit string array

six_bit_array = [bit_string[i:i+6] for i in range(0, len(bit_string), 6)]
print(six_bit_array)
#get integer arrray
integer_array = [int(i,2) for i in six_bit_array]
print(integer_array)

# map to base64
base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
my_b64 = ''
for i in integer_array:
  my_b64 = my_b64 + base64chars[i]
print()
print(my_b64)
    #print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i))

a = c.decode( Modulus, 'hex')
b = b64(a)
c = b.decode()
#print(a)
#print(b)
print()
print(c)

from base64 import urlsafe_b64decode as urlb64_d , b64decode as b64_d


data = {"x5c": [
"MIIDBzCCAe+gAwIBAgIJakoPho0MJr56MA0GCSqGSIb3DQEBCwUAMCExHzAdBgNVBAMTFmRldi1lanRsOTg4dy5hdXRoMC5jb20wHhcNMTkxMDI5MjIwNzIyWhcNMzMwNzA3MjIwNzIyWjAhMR8wHQYDVQQDExZkZXYtZWp0bDk4OHcuYXV0aDAuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzkM1QHcP0v8bmwQ2fd3Pj6unCTx5k8LsW9cuLtUhAjjzRGpSEwGCKEgi1ej2+0Cxcs1t0wzhO+zSv1TJbsDI0x862PIFEs3xkGqPZU6rfQMzvCmncAcMjuW7r/Zewm0s58oRGyic1Oyp8xiy78czlBG03jk/+/vdttJkie8pUc9AHBuMxAaV4iPN3zSi/J5OVSlovk607H3AUiL3Bfg4ssS1bsJvaFG0kuNscoiP+qLRTjFK6LzZS99VxegeNzttqGbtj5BwNgbtuzrIyfLmYB/9VgEw+QdaQHvxoAvD0f7aYsaJ1R6rrqxo+1Pun7j1/h7kOCGB0UcHDLDw7gaP/wIDAQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBQwIoo6QzzUL/TcNVpLGrLdd3DAIzAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBALb8QycRmauyC/HRWRxTbl0w231HTAVYizQqhFQFl3beSQIhexGik+H+B4ve2rv94QRD3LlraUp+J26wLG89EnSCuCo/OxPAq+lxO6hNf6oKJ+Y2f48awIOxolO0f89qX3KMIkABXwKbYUcd+SBHX5ZP1V9cvJEyH0s3Fq9ObysPCH2j2Hjgz3WMIffSFMaO0DIfh3eNnv9hKQwavUO7fL/jqhBl4QxI2gMySi0Ni7PgAlBgxBx6YUp59q/lzMgAf19GOEOvI7l4dA0bc9pdsm7OhimskvOUSZYi5Pz3n/i/cTVKKhlj6NyINkMXlXGgyM9vEBpdcIpOWn/1H5QVy8Q="
]}


for i in data['x5c']:
  print(b64_d(i))
  with open('x5c.der', "wb") as f:
      f.write(b64_d(i))

data = 'MIIEmDCCAwACCQDIHIjyvbwAUjANBgkqhkiG9w0BAQsFADCBjTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVNhdXNhbGl0bzEVMBMGA1UECgwMSGVhbHRoZURhdGExMRcwFQYDVQQDDA5FcmljIEhhYXMsIERWTTElMCMGCSqGSIb3DQEJARYWZWhhYXNAaGVhbHRoZWRhdGExLm9yZzAeFw0yMTEwMDYwODQ1MDhaFw0yMjEwMDEwODQ1MDhaMIGNMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJU2F1c2FsaXRvMRUwEwYDVQQKDAxIZWFsdGhlRGF0YTExFzAVBgNVBAMMDkVyaWMgSGFhcywgRFZNMSUwIwYJKoZIhvcNAQkBFhZlaGFhc0BoZWFsdGhlZGF0YTEub3JnMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA4zj0+VAonuMM7K/YZeVvKviGqRdsFo9M2XDtsnn1Rsx26hx/DhIBgLLwmgoXfIj1vmsNEJtuHRy0WlxKNbRvZDtQBh/47HNfGaLsqJj3K9WYmmy+AjNZi0PABj15KvditwvXIjo+44FpWNtjvtuvGJ+GiuXjEx4A5/IJXFQHTuDBPtM2zvErZzabaYDvbZyURci3DC96krS9f8pcY8LoSmtDW0y1cDb1rBpbIDdepLrWLQau03A7Wufc1day2PUP3ulZnzl83BNibiIKMK1jFi3zLa/XisXrRqxTQAqIMISpzyNFxGLOwiZac3Pkg85YnveWkxjsO8xDJ9aYl2DIJCefDby9pJn58KIjW6pXGDH07LvQ0kTCXuSHV0ZYoiEkvN2nnNhTSgluB6Nn99EgSs4J+RyNR08Z4T4bQvs68yUCK0uqGbNrRqcluaUUUxDHJdJ2UB9kRPxqE9g0MzG7xJ+fIus8Ppo5VYnvIxg7WhOnHQjybDmsarORwrpYMZ7tAgMBAAEwDQYJKoZIhvcNAQELBQADggGBAN5cCACfP1gFDdyVMt+xHRKUvbdMW9J3QFUfMMh7NguIVELtb80xpiVoRoeqcclQMWkocU5UGhmi9DMqb0ZGVbiMDNGwaIBerI6g5ZzdeDnH9bhIN0FWH5KafvVeOWca+vpKAqFmuc9SwpDGH2Oz5ZPdOaLjEK3gZ9DIbX50/T2f+oP/r1dirzYVEpsmU3LSoLLRx8uOoncFHxamlqKCQNmRM8emnYFQhgkQGAAEmr41ZZs88PqMiL6Fdl60n+oJU3eyO6siF8FBwzJl4epHSBBxkq/JcQhAPojqBPnpecwhl3ud5x1q+YO1Mso9mbEVqrJYXIZg4UBK4EfHqzTGpfpik9Jp7Gd6sAoqubpLNX8bY40rWgMP0IpZcRlUd5pSzYa/LKMAyz4p12muvUuuR6wmNDJ+Kz4aGf1TeJYsXXHGUee6GWzvLaV1I6rc/xyDn8mdw9CbbtbHPwa1r2Nv8bpnRvFyd0FsKgXBcrY5pbpFQWwc/+p4fxM4x1kRly4ZPA=='

print(b64_d(data))

# ERICS-AIR-2:venv ehaas$ openssl x509 -in x5c.der  -inform DER -text to read bytes in bash

# Certificate:
#     Data:
#         Version: 3 (0x2)
#         Serial Number:
#             6a:4a:0f:86:8d:0c:26:be:7a
#     Signature Algorithm: sha256WithRSAEncryption
#         Issuer: CN=dev-ejtl988w.auth0.com
#         Validity
#             Not Before: Oct 29 22:07:22 2019 GMT
#             Not After : Jul  7 22:07:22 2033 GMT
#         Subject: CN=dev-ejtl988w.auth0.com
#         Subject Public Key Info:
#             Public Key Algorithm: rsaEncryption
#                 Public-Key: (2048 bit)
#                 Modulus:
#                     00:ce:43:35:40:77:0f:d2:ff:1b:9b:04:36:7d:dd:
#                     cf:8f:ab:a7:09:3c:79:93:c2:ec:5b:d7:2e:2e:d5:
#                     21:02:38:f3:44:6a:52:13:01:82:28:48:22:d5:e8:
#                     f6:fb:40:b1:72:cd:6d:d3:0c:e1:3b:ec:d2:bf:54:
#                     c9:6e:c0:c8:d3:1f:3a:d8:f2:05:12:cd:f1:90:6a:
#                     8f:65:4e:ab:7d:03:33:bc:29:a7:70:07:0c:8e:e5:
#                     bb:af:f6:5e:c2:6d:2c:e7:ca:11:1b:28:9c:d4:ec:
#                     a9:f3:18:b2:ef:c7:33:94:11:b4:de:39:3f:fb:fb:
#                     dd:b6:d2:64:89:ef:29:51:cf:40:1c:1b:8c:c4:06:
#                     95:e2:23:cd:df:34:a2:fc:9e:4e:55:29:68:be:4e:
#                     b4:ec:7d:c0:52:22:f7:05:f8:38:b2:c4:b5:6e:c2:
#                     6f:68:51:b4:92:e3:6c:72:88:8f:fa:a2:d1:4e:31:
#                     4a:e8:bc:d9:4b:df:55:c5:e8:1e:37:3b:6d:a8:66:
#                     ed:8f:90:70:36:06:ed:bb:3a:c8:c9:f2:e6:60:1f:
#                     fd:56:01:30:f9:07:5a:40:7b:f1:a0:0b:c3:d1:fe:
#                     da:62:c6:89:d5:1e:ab:ae:ac:68:fb:53:ee:9f:b8:
#                     f5:fe:1e:e4:38:21:81:d1:47:07:0c:b0:f0:ee:06:
#                     8f:ff
#                 Exponent: 65537 (0x10001)
#         X509v3 extensions:
#             X509v3 Basic Constraints: critical
#                 CA:TRUE
#             X509v3 Subject Key Identifier:
#                 30:22:8A:3A:43:3C:D4:2F:F4:DC:35:5A:4B:1A:B2:DD:77:70:C0:23
#             X509v3 Key Usage: critical
#                 Digital Signature, Certificate Sign
#     Signature Algorithm: sha256WithRSAEncryption
#          b6:fc:43:27:11:99:ab:b2:0b:f1:d1:59:1c:53:6e:5d:30:db:
#          7d:47:4c:05:58:8b:34:2a:84:54:05:97:76:de:49:02:21:7b:
#          11:a2:93:e1:fe:07:8b:de:da:bb:fd:e1:04:43:dc:b9:6b:69:
#          4a:7e:27:6e:b0:2c:6f:3d:12:74:82:b8:2a:3f:3b:13:c0:ab:
#          e9:71:3b:a8:4d:7f:aa:0a:27:e6:36:7f:8f:1a:c0:83:b1:a2:
#          53:b4:7f:cf:6a:5f:72:8c:22:40:01:5f:02:9b:61:47:1d:f9:
#          20:47:5f:96:4f:d5:5f:5c:bc:91:32:1f:4b:37:16:af:4e:6f:
#          2b:0f:08:7d:a3:d8:78:e0:cf:75:8c:21:f7:d2:14:c6:8e:d0:
#          32:1f:87:77:8d:9e:ff:61:29:0c:1a:bd:43:bb:7c:bf:e3:aa:
#          10:65:e1:0c:48:da:03:32:4a:2d:0d:8b:b3:e0:02:50:60:c4:
#          1c:7a:61:4a:79:f6:af:e5:cc:c8:00:7f:5f:46:38:43:af:23:
#          b9:78:74:0d:1b:73:da:5d:b2:6e:ce:86:29:ac:92:f3:94:49:
#          96:22:e4:fc:f7:9f:f8:bf:71:35:4a:2a:19:63:e8:dc:88:36:
#          43:17:95:71:a0:c8:cf:6f:10:1a:5d:70:8a:4e:5a:7f:f5:1f:
#          94:15:cb:c4
# -----BEGIN CERTIFICATE-----
# MIIDBzCCAe+gAwIBAgIJakoPho0MJr56MA0GCSqGSIb3DQEBCwUAMCExHzAdBgNV
# BAMTFmRldi1lanRsOTg4dy5hdXRoMC5jb20wHhcNMTkxMDI5MjIwNzIyWhcNMzMw
# NzA3MjIwNzIyWjAhMR8wHQYDVQQDExZkZXYtZWp0bDk4OHcuYXV0aDAuY29tMIIB
# IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzkM1QHcP0v8bmwQ2fd3Pj6un
# CTx5k8LsW9cuLtUhAjjzRGpSEwGCKEgi1ej2+0Cxcs1t0wzhO+zSv1TJbsDI0x86
# 2PIFEs3xkGqPZU6rfQMzvCmncAcMjuW7r/Zewm0s58oRGyic1Oyp8xiy78czlBG0
# 3jk/+/vdttJkie8pUc9AHBuMxAaV4iPN3zSi/J5OVSlovk607H3AUiL3Bfg4ssS1
# bsJvaFG0kuNscoiP+qLRTjFK6LzZS99VxegeNzttqGbtj5BwNgbtuzrIyfLmYB/9
# VgEw+QdaQHvxoAvD0f7aYsaJ1R6rrqxo+1Pun7j1/h7kOCGB0UcHDLDw7gaP/wID
# AQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBQwIoo6QzzUL/TcNVpL
# GrLdd3DAIzAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBALb8QycR
# mauyC/HRWRxTbl0w231HTAVYizQqhFQFl3beSQIhexGik+H+B4ve2rv94QRD3Llr
# aUp+J26wLG89EnSCuCo/OxPAq+lxO6hNf6oKJ+Y2f48awIOxolO0f89qX3KMIkAB
# XwKbYUcd+SBHX5ZP1V9cvJEyH0s3Fq9ObysPCH2j2Hjgz3WMIffSFMaO0DIfh3eN
# nv9hKQwavUO7fL/jqhBl4QxI2gMySi0Ni7PgAlBgxBx6YUp59q/lzMgAf19GOEOv
# I7l4dA0bc9pdsm7OhimskvOUSZYi5Pz3n/i/cTVKKhlj6NyINkMXlXGgyM9vEBpd
# cIpOWn/1H5QVy8Q=
# -----END CERTIFICATE-----

#  create fingerprint from certifcates using
# openssl x509 -noout -in  x5c.der -fingerprint > my_fingerprint  <____DOES not work  get error
# PEM routines:CRYPTO_internal:
# no start line:/BuildRoot/Library/Caches/com.apple.xbs/Sources/libressl/libressl-22.260.1/libressl-2.6/crypto/pem/pem_lib.c:683:Expecting:
# TRUSTED CERTIFICATE

# SHA256 Fingerprint=4E:D7:C3:DD:19:43:DE:8A:0C:01:AC:E5:48:45:60:E3:12:B5:44:07:F2:0B:C9:A6:30:BA:98:73:29:38:58:D9

my_b64 = b64(b'foo')
print(my_b64,urlb64_d(my_b64) )
