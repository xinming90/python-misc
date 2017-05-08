# -*- coding: utf-8 -*-


def test_for_else():
    def find(seq, target):
        found = False
        for i, value in enumerate(seq):
            if value == target:
                found = True
                break
        if not found:
            return -1
        return i

    def find_for_else(seq, targe):
        for i, value in enumerate(seq):
            if value == targe:
                break
        else:
            return -1
        return i

    assert find('abc', 'a') == find_for_else('abc', 'a')
    assert find('abc', 'c') == find_for_else('abc', 'c')
    assert find('abc', 'd') == find_for_else('abc', 'd')
