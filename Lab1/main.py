import hashlib
import hmac
from Crypto.Hash import KMAC128


# def hash256(p):
#     m = p.encode()  # Concerts text to byte code (UTF-8) - Unicode representation
#     # tion
#     h = hashlib.sha256(m)  # converts to binary representation
#     return h.hexdigest()  # calls the hex version of the output
#     # return hashlib.sha256(p.encode("utf-8")).hexdigest()
# def hashShaw3_256(p):
#     m = p.encode()
#     h = hashlib.sha3_256(m)
#     return h.hexdigest()
# def hashShake256(p):
#     m = p.encode()
#     h = hashlib.shake_256(m)
#     return h.hexdigest(32)
# def main():
#     w = "helloworld"
#     print(w)
#     print(f"SHA-256   {hash256(w)}")
#     print(f"SHA3-256  {hashShaw3_256(w)}")
#     print(f"SHAKE-256 {hashShake256(w)}")
# main()
# print(hashlib.algorithms_available)
# print('helloworld'.encode()) # print of encoded value
# print(hashlib.sha256('helloworld'.encode())) # Gets the address of the hash object, not the actual hex
# print(hashlib.sha256('helloworld'.encode()).hexdigest()) # Returns the hex (hash) value [digest]

def main():
    w = 'helloworld'
    w2 = w.encode() # converting the string to byte code

    print(f"        SHA-256 {hashlib.sha256(w2).hexdigest()}")
    print(f"       SHA3-256 {hashlib.sha3_256(w2).hexdigest()}")
    print(f"      SHAKE-256 {hashlib.shake_256(w2).hexdigest(32)}")
    w3 = w2 + b'apple'#.encode()
    print(f"     cShakeLike {hashlib.shake_256(w3).hexdigest(32)}") # cShake

    print("\n------- Tuple -------") # example of tuple hash
    acct = '5001'
    amt = '50'
    inputString = str(len(acct)) + acct + str(len(amt)) + amt
    print(f"      SHAKE-256 {hashlib.shake_256(inputString.encode()).hexdigest(32)}")

    # implementing HMAC prepend msg with secret
    print("\n------- HMAC -------")
    secret = b'secret'
    print(f"HMAC authN tag: {hmac.new(secret, w2, hashlib.sha256).hexdigest()}") #pass in secret, msg, algorithm (sha256)
    print(f"HMAC authN tag: {hmac.new(secret, w2, hashlib.sha512).hexdigest()}") #pass in secret, msg, algorithm (sha512)

    # w3 had a customization string added
    # print(f"HMAC authN tag: {hmac.new(secret, w2, hashlib.cShake).hexdigest(16)}")

    secret = b'Sixteen byte key'
    mac = KMAC128.new(key=secret, mac_len=32)
    mac.update(b'Hello')
    print(f"\t\t  KMAC: {mac.hexdigest()}")

main()


