import jwt

jwt_encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"


jwt.decode(jwt_encoded, options={"verify_signature": False})




JWTs are broken to three parts separated by . the first part is the header, the second is the payload, and the last one is the signature.

Both the header and payload can easily be decrypted to see its plaintext value. The signature, on the other hand, is encrypted with a 256-bit secret key.

You can use online tools like this one in order to decode JWTs but since the challenge recommended that we use PyJWT in order to prepare us for future challenges, we’re going to use that.
