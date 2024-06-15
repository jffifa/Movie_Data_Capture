import requests

_session = None


def set_session(value=None):
    global _session
    _session = value


def get_session():
    global _session
    if _session is None:
        _session = requests.Session()

    return _session
