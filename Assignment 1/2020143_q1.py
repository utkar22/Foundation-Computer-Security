#FCS Assignment 1, question 1
#Name: Utkarsh Arora
#Roll number: 2020143

from Crypto.Cipher import Salsa20
import gmpy2
import os

def check_e(e, z):
    '''
    Helper function to find e.
    We know that e and z must be coprime.
    The generated d must be different from e.
    And d must be coprime to z.
    '''
    d = gmpy2.invert(e,z)

    if (gmpy2.gcd(d, z)!=1):
        return False
    elif (e==d):
        return False
    else:
        return d

def find_d(z):
    '''
    Helper function to find d
    '''
    #We are not allowed to use loops to find e and d. Hence, I have essentially
    #hard coded some values, and ran verification checks to find the suitable keys

    if (z>100003):
        d = check_e(100003, z)

        if (d):
            return 100003, d

    if (z>65537):
        d = check_e(65537, z)

        if (d):
            return 65537, d

    if (z>22543):
        d = check_e(22543, z)

        if (d):
            return 22543, d

    if (z>10007):
        d = check_e(10007, z)

        if (d):
            return 10007, d

    if (z>7877):
        d = check_e(7877, z)

        if (d):
            return 7877, d

    if (z>1847):
        d = check_e(1847, z)

        if (d):
            return 1847, d

    if (z>1051):
        d = check_e(1051, z)

        if (d):
            return 1051, d

    if (z>751):
        d = check_e(751, z)

        if (d):
            return 751, d

    if (z>257):
        d = check_e(257, z)

        if (d):
            return 257, d

    if (z>101):
        d = check_e(101, z)

        if (d):
            return 101, d

    if (z>73):
        d = check_e(73, z)

        if (d):
            return 73, d

    if (z>17):
        d = check_e(17, z)

        if (d):
            return 17, d

    if (z>7):
        d = check_e(7, z)

        if (d):
            return 7, d

    if (z>5):
        d = check_e(5, z)

        if (d):
            return 5, d

    if (z>3):
        d = check_e(3, z)

        if (d):
            return 3, d

    return 0

    
    

def alice_generates_symmetric_key():
    ''' 
    A function that returns a 16 byte string to be used as the key for Salsa20.
    This key should be used to encrypt Bob and Alice's communications.
    But before that, it needs to be sent to Bob.

    Input: NA
    Return: the symmetric key (byte string)
    '''
    return b"\x00"+os.urandom(16)+b"\x00"

def bob_generates_asymmetric_keys(p ,q):
    '''
    A function that takes in prime numbers p and q and generates 
    the public and private keys for Bob as per RSA. Note that you are 
    not allowed to use loops to find e or d.

    Input: p, q (upto 1023 digits long)
    Return: Bob's public key and private key ((e,n), (d,n)) as a tuple
    '''
    #n = p*q
    #z = (p-1)*(q-1)
    #e and z are coprime
    #ed mod z = 1
    
    n = gmpy2.mpz(p)*gmpy2.mpz(q)
    z = gmpy2.mpz(p-1)*gmpy2.mpz(q-1)

    e, d = find_d(z)

    e = gmpy2.mpz(e)

    return ((e,n), (d,n))
    
    

    
    

def alice_sends_symmetric_key(k, e, n):
    '''
    A function that Alice uses to encrypt the symmetric key
    using Bob's public key. The ciphertext is sent to Bob.

    Input: the symmetric key k, Bob's public key e, n.
    Return: encrypted ciphertext
    '''
    k = int.from_bytes(k, "big")
    return gmpy2.powmod(k,e,n)


def bob_decrypts_symmetric_key(c, d, n):
    '''
    A function that Bob uses to decrypt the ciphertext c using his private key.
    The decrypted message would give him the symmetric key.

    Input: the ciphertext c, Bob's private key d, n.
    Return: the symmetric key (byte string)
    '''
    c = int.from_bytes(c, "big")
    k = gmpy2.powmod(c,d,n)
    k = gmpy2.to_binary(k)
    return k

def bob_sends_message(m, k):
    '''
    A function that takes a message m, shared key k and uses Salsa20 to encrypt m.

    Input: the message m (a byte string), the shared key k (byte string)
    Return: encrypted ciphertext
    '''
    cipher = Salsa20.new(key = k)
    msg = cipher.nonce + cipher.encrypt(m)
    return msg

def alice_decrypts_message(c_, k):
    '''
    A function that takes an encrypted message c_, shared key k and uses Salsa20 to decrypt c_.

    Input: the ciphertext c_, the shared key k (byte string)
    Return: plaintext message
    '''
    msg_nonce = c_[:8]
    cipher_text = c_[8:]
    #text = bytes(cipher_text, 'utf-8')
    cipher = Salsa20.new(key = k, nonce = msg_nonce)
    decrypted = cipher.decrypt(cipher_text)

    #for i in decrypted:
    #    print(i)
    plaintext = decrypted.decode(encoding="utf-8")
    return plaintext

if __name__=="__main__":
    # p, q and the message m will be taken as inputs from the user.
    p = int(input("p: "))
    q = int(input("q: "))
    plaintext = input("Message: ")

    k = alice_generates_symmetric_key()
    #k = int.from_bytes(k, "big")
    #k = gmpy2.mpz(k)
    print(f"Symmetric key: {k}")

    pub_key, priv_key = bob_generates_asymmetric_keys(p, q)

    print(f"Public key: {pub_key}")
    print(f"Private key: {priv_key}")

    e,n = pub_key
    d,n = priv_key

    c = alice_sends_symmetric_key(k, e, n)
    print(f"Encrypted symmetric key: {c}")

    c = gmpy2.to_binary(c)

    k = bob_decrypts_symmetric_key(c, d, n)
    print(f"Decrypted symmetric key: {k}")
    
    #k = int(k)
    #k = k.to_bytes(2,byteorder='big')
    #k = gmpy2.to_binary(k)
    k = k[:16]

    m = bytes(plaintext, 'utf-8')
    

    c_ = bob_sends_message(m, k)
    print(f"Encrypted ciphertext: {c}")

    #c_ = c_.to_bytes(2,byteorder='big')

    plaintext = alice_decrypts_message(c_, k)
    print(f"Decrypted plaintext: {plaintext}")
