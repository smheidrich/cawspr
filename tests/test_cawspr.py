from cawspr import replace_all


def test_replace_all():
    assert (
        replace_all("hello world", {"hel": "f", "f": "definitely not"}.items())
        == "flo world"
    )
