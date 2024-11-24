from Crypto.PublicKey import RSA
f = open("alicepublic.pem", "r")
key = RSA.importKey(f.read())
print(key.n) #displays n
print(key.e) #displays e