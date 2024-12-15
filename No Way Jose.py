import base64
import json
import jwt # note this is the PyJWT module, not python-jwt


SECRET_KEY = ?
FLAG = ?


@chal.route('/no-way-jose/authorise/<token>/')
def authorise(token):
    token_b64 = token.replace('-', '+').replace('_', '/') # JWTs use base64url encoding
    try:
        header = json.loads(base64.b64decode(token_b64.split('.')[0] + "==="))
    except Exception as e:
        return {"error": str(e)}

    if "alg" in header:
        algorithm = header["alg"]
    else:
        return {"error": "There is no algorithm key in the header"}

    if algorithm == "HS256":
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except Exception as e:
            return {"error": str(e)}
    elif algorithm == "none":
        try:
            decoded = jwt.decode(token, algorithms=["none"], options={"verify_signature": False})
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Cannot decode token"}

    if "admin" in decoded and decoded["admin"]:
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}


@chal.route('/no-way-jose/create_session/<username>/')
def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': False}, SECRET_KEY, algorithm='HS256')
    return {"session": encoded}


As mentioned on the first challenge, Token Appreciation, the first part of JWT is the JOSE header.

This is where you indicate that this is a JWT and what algorithm was used for the encryption. According to the challenge, this is a major flaw since a server have to process this untrusted payload before verifying the JWT as a whole, enabling us to essentially bypass authorization by manipulating the contents of this header.

The No Way Jose challenge will present you with a code. You can play with it using different usernames and see if you can be verified as an admin.

First, generate a JWT using the admin username. If we decode the generated JWT, it will do the encode and decode ad header and Payload.The nice thing about jwt.io is that we can edit the contents of the payload. So, change the admin value to true


