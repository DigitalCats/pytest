# -*-coding:utf-8-*-
import pytest


@pytest.fixture
def begin():
    print('开始')
    yield
    print ('结束')