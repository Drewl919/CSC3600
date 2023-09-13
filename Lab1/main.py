import hashlib

def hash(p):
    m = p.encode() # Concerts text to byte code
    h = hashlib.sha256(m).hexdigest() # converts to binary representation, then calls the hex version of the output
    return h
    # return hashlib.sha256(p.encode("utf-8")).hexdigest()

def main() :
    w = "helloworld"
    print(w)
    print(hash(w))

main()