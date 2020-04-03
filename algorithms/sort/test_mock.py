from unittest.mock import MagicMock


def test_mock():
    class ProductionClass:
        pass
    thing = ProductionClass()
    thing.method = MagicMock(return_value=3)
    assert thing.method(3, 4, 5, key='value') == 3
    thing.method.assert_called_with(3, 4, 5, key='value')


def test_mock_sort():
    mocksort = MagicMock(return_value=['a', 'b', 'c', 'd'])
    assert mocksort() == ['a', 'b', 'c', 'd']
