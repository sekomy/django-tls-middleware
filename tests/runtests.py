#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_sqlite'

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(path)

    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["test_tls_middleware"])
    sys.exit(bool(failures))
