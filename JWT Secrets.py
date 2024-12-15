import jwt # note this is the PyJWT module, not python-jwt


SECRET_KEY = ? # TODO: PyJWT readme key, change later
FLAG = ?


@chal.route('/jwt-secrets/authorise/<token>/')
def authorise(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        return {"error": str(e)}

    if "admin" in decoded and decoded["admin"]:
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}


@chal.route('/jwt-secrets/create_session/<username>/')
def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': False}, SECRET_KEY, algorithm='HS256')
    return {"session": encoded}

import jwt

key = "secret"
encoded = jwt.encode({"username":"admin","admin":True}, key, algorithm="HS256")

print(encoded)


Main advantage of JWTs as opposed to session ID is that JWTs live on the client side and it’s easier to scale. Different back end servers can authorize a single JWT instead of having to create multiple session object per server.
