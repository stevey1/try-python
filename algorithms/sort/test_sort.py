from sort import Sort

from insert_sort import sort as insert_sort
from selection_sort import sort as selection_sort
from merge_sort import sort as merge_sort
from quick_sort import sort as quick_sort
#from bubble_sort import sort as bubble_sort
sort = Sort()


def test_insert_sort():
    a = ['d', 'a', 'c', 'b']
    insert_sort(a)
    assert a == ['a', 'b', 'c', 'd']


def test_selection_sort():
    assert selection_sort(['d', 'a', 'c', 'b']) == ['a', 'b', 'c', 'd']


def test_merge_sort():
    a = ['d', 'a', 'c', 'b']
    Sort.merge_sort(a)
    assert a == ['a', 'b', 'c', 'd']


def test_qucik_sort():
    b = ['d', 'e', 'a', 'c', 'b']
    quick_sort(b, 0, len(b)-1)
    assert b == ['a', 'b', 'c', 'd', 'e']


def test_bubble_sort():
    b = ['d', 'a', 'c', 'b']
    Sort.bubble_sort(b)
    assert b == ['a', 'b', 'c', 'd']
