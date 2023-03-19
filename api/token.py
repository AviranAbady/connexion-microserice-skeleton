from connexion import request
import logging as logger


def get_tokeninfo():
    try:
        _, access_token = request.headers["Authorization"].split()
    except Exception:
        logger.info("Could not extract authorization token")
        return "", 401

    uid = '123456789'

    return {"uid": uid, "scope": ["uid"]}
