from os import path
from tempfile import TemporaryDirectory, mkdtemp

from django.test import TestCase, override_settings

fake_media_root = mkdtemp()
TemporaryDirectory


class MyTestCase(TestCase):
    @override_settings(MEDIA_ROOT=fake_media_root)
    def test_1(cls):
        pass

    def tearDownClass(cls):
        path().re


def run(*args, **kwargs):
    print(*args, **kwargs)
