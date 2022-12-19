#!/usr/bin/env python3
from sys import argv, stdin
from typing import Sequence, Tuple


def to_space_sep_words(words: Sequence[str]) -> str:
    return " ".join(words)


def to_snake_case(words: Sequence[str]) -> str:
    return "_".join(words)


def to_screaming_snake_case(words: Sequence[str]) -> str:
    return "_".join([word.upper() for word in words])


def to_camel_case(words: Sequence[str]) -> str:
    return "".join([word.capitalize() for word in words])


def to_lower_camel_case(words: Sequence[str]) -> str:
    return "".join(words[:1] + [word.capitalize() for word in words[1:]])


def replace_all(s: str, old_to_new: Tuple[str, str]) -> str:
    """
    Simultaneous, non-overlapping execution of multiple string replacements.
    """
    range_to_old_and_new = {}
    for old, new in old_to_new:
        end = 0
        while True:
            start = s.find(old, end)
            if start == -1:
                break
            end = start + len(old)
            if any(
                start in range_ for range_ in range_to_old_and_new.keys()
            ) or any(end in range_ for range_ in range_to_old_and_new.keys()):
                continue
            range_to_old_and_new[range(start, end)] = (old, new)
    new_s_list = []
    last_end = 0
    for range_, (old, new) in sorted(
        range_to_old_and_new.items(), key=lambda x: x[0].start
    ):
        new_s_list.append(s[last_end : range_.start])
        new_s_list.append(s[range_.start : range_.stop].replace(old, new))
        last_end = range_.stop
    new_s_list.append(s[last_end:])
    return "".join(new_s_list)


if __name__ == "__main__":
    old = argv[1]
    new = argv[2]

    old_words = old.split(" ")
    new_words = new.split(" ")

    inp = stdin.read()

    mapping = [
        (caws_func(old_words), caws_func(new_words))
        for caws_func in [
            to_space_sep_words,
            to_snake_case,
            to_screaming_snake_case,
            to_camel_case,
            to_lower_camel_case,
        ]
    ]

    outp = replace_all(inp, mapping)

    print(outp, end="")
