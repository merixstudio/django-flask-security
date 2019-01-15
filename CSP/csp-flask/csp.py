from flask import make_response

from functools import wraps

__all__ = ('csp',)


# Rules for Content Security Policy. This is a dictionary consisting of a key which is directive
# (like default-src or script-src) and a list or tuple of policies. See https://www.w3.org/TR/CSP2/
# for further reference. Note that this solution is only intended to serve demonstration purposes,
# which means it is not suitable for production environment.
SETTINGS_CSP = {
    'default-src': [
        '\'self\'',
    ],
    'script-src': [
        '\'self\'',
        '\'sha256-pu1SeSVRQwuLmgKFdpgMzTi7ghm2F3Ldi/iw1Ff6Myc=\''
    ]
}

# Same rules for CSP, except for this will only report violations.
SETTINGS_REPORT_CSP = {}
REPORT_URI = '/report-csp-violations'


def make_csp_header(settings, report_uri=None):
    header = ''
    for directive, policies in settings.items():
        header += f'{directive} '
        header += ' '.join(
            (policy for policy in policies)
        )
        header += ';'
    if report_uri:
        header += f' report-uri {report_uri}'
    return header


def csp(func):
    @wraps(func)
    def _csp(*args, **kwargs):
        response = make_response(func(*args, **kwargs))
        if SETTINGS_REPORT_CSP:
            response.headers[
                'Content-Security-Policy-Report-Only'
            ] = make_csp_header(SETTINGS_REPORT_CSP, REPORT_URI)
        if SETTINGS_CSP:
            response.headers[
                'Content-Security-Policy'
            ] = make_csp_header(SETTINGS_CSP, REPORT_URI)
        return response
    return _csp

