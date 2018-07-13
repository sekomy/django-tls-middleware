from django.test import RequestFactory
from django.test import SimpleTestCase

from tls_middleware import get_request


class TLSMiddlewareTest(SimpleTestCase):
    request = RequestFactory().request()

    @property
    def middleware(self):
        from tls_middleware import TLSMiddleware
        return TLSMiddleware()

    @property
    def response(self, *args, **kwargs):
        from django.http import HttpResponse
        return HttpResponse(*args, **kwargs)

    def test_tls_middleware_process_request(self):
        from django.core.handlers.wsgi import WSGIRequest

        self.middleware.process_request(self.request)

        self.assertIsInstance(get_request(), WSGIRequest)
        self.assertEqual(get_request(), self.request)

    def test_tls_middleware_process_response(self):
        self.middleware.process_response(self.request, self.response)

        self.assertIsNone(get_request())
