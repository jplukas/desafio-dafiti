# from django.test import TestCase
import pytest

from myblog.templatetags.blog_extratags import intdiv

# Create your tests here.


@pytest.mark.parametrize(
    'value, arg, result',
    [(100, 10, 10), (50, 5, 10), (26, 13, 2), (11, 10, 1), (20, 3, 6)],
)
def test_readtime(value, arg, result):
    assert intdiv(value, arg) == result
