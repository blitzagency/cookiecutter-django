from django.test import TestCase
from django.core.cache import cache


def test_cache(client):
    cache.set('test_cache', 42)
    assert cache.get('test_cache') ==  42

def test_cache2(admin_client):
    pass
