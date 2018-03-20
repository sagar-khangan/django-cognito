from warrant import Cognito

USER_POOL = ''
CLIENT_ID= ''


def get_user_pool():
    return USER_POOL

def get_client_id():
    return CLIENT_ID

def get_cognito_obj(username,access_token = None):
    if access_token:
        u = Cognito(USER_POOL, CLIENT_ID, username=username,access_token=access_token)
    else:
        u = Cognito(USER_POOL, CLIENT_ID, username=username)
    return u

