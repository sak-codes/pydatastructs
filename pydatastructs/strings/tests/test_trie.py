from pydatastructs import Trie

def test_Trie():

    strings = ["A", "to", "tea", "ted", "ten", "i",
               "in", "inn", "Amfn", "snbr"]
    trie = Trie()
    for string in strings:
        trie.insert(string)

    prefix_strings = ["te", "t", "Am", "snb"]

    for string in strings:
        assert trie.is_inserted(string)

    for string in prefix_strings:
        assert trie.is_present(string)
        assert not trie.is_inserted(string)

    assert sorted(trie.strings_with_prefix("t")) == ['tea', 'ted', 'ten', 'to']
    assert sorted(trie.strings_with_prefix("te")) == ["tea", "ted", "ten"]
    assert trie.strings_with_prefix("i") == ["i", "in", "inn"]
    assert trie.strings_with_prefix("a") == []

    remove_order = ["to", "tea", "ted", "ten", "inn", "in", "A"]

    assert trie.delete("z") is None

    for string in remove_order:
        trie.delete(string)
        for present in strings:
            if present == string:
                assert not trie.is_inserted(present)
            else:
                assert trie.is_inserted(present)
        strings.remove(string)
     