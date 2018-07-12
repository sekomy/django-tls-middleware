from .tls import _tls


def get_user():
    """
    :return: User
   """

    return getattr(_tls, 'user', None)


def get_request():
    """
    :return: <WSGIRequest:>
    """
    return getattr(_tls, 'request', None)
