def jwt_response_payload_handler(token, user=None, request=None):
    """
    Custom response payload handler.
    This function controlls the custom payload after login or token refresh. This data is returned through the web API.
    """
    responseObj = {
        'token'     : token,
        'is_student': user.is_student,
        'is_mentor' : user.is_mentor,
        'username'  : user.username
    }
    if user.is_student:
        responseObj['user_id'] = user.student.id
    elif user.is_mentor:
        responseObj['user_id'] = user.mentor.id
    return responseObj