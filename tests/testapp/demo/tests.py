# -*- coding: utf-8 -*-
from django.core.handlers.wsgi import WSGIRequest
from django.test import TestCase
from django.test import RequestFactory
from .views import TestView
from tls_middleware.utils import get_request
from tls_middleware.tls import TLSMiddleware


class TestTLSMiddleware(TestCase):
    def setUp(self):
        def factory(url):
            return RequestFactory().get(url)

        self.tls_middleware = TLSMiddleware()
        self.test_view = TestView()
        self.request = factory('/')

    def test_tls_middleware_process_request(self):
        self.tls_middleware.process_request(self.request)

        self.assertIsInstance(get_request(), WSGIRequest)
        self.assertEqual(get_request(), self.request)

    def test_tls_middleware_process_response(self):
        response = self.test_view.get(self.request)
        self.tls_middleware.process_response(self.request, response)

        self.assertIsNone(get_request())
