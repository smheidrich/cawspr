#!/usr/bin/env python3
from sys import stdin
from typing import MutableMapping, Sequence, Tuple

import typer


def to_space_sep_words(words: Sequence[str]) -> str:
    return " ".join(words)


def to_snake_case(words: Sequence[str]) -> str:
    return "_".join(words)


def to_kebab_case(words: Sequence[str]) -> str:
    return "-".join(words)


def to_screaming_snake_case(words: Sequence[str]) -> str:
    return "_".join([word.upper() for word in words])


def to_camel_case(words: Sequence[str]) -> str:
    return "".join([word.capitalize() for word in words])


def to_lower_camel_case(words: list[str]) -> str:
    return "".join(words[:1] + [word.capitalize() for word in words[1:]])


def replace_all(s: str, old_to_new: Sequence[Tuple[str, str]]) -> str:
    """
    Simultaneous, non-overlapping execution of multiple string replacements.
    """
    range_to_old_and_new: MutableMapping[range, Tuple[str, str]] = {}
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


app = typer.Typer()


@app.command()
def main(
    words_to_replace: str = typer.Argument(
        ..., help="words to replace (lowercase, space-separated)"
    ),
    replace_with: str = typer.Argument(
        ..., help="words to replace them with (lowercase, space-separated)"
    ),
) -> None:
    """
    Case And Word Separation Preserving Replace (CAWSPR)

    Replace a multi-word string with another, preserving the manner in which
    the words are joined together (e.g. snake_case, CamelCase, lowerCamelCase,
    ...) in each occurrence.

    Reads from standard input and outputs to standard output.
    Currently only supports UTF-8 encoded text but that should change soon.
    """
    old_words = words_to_replace.split(" ")
    new_words = replace_with.split(" ")

    inp = stdin.read()

    mapping = [
        (caws_func(old_words), caws_func(new_words))
        for caws_func in [
            to_space_sep_words,
            to_snake_case,
            to_kebab_case,
            to_screaming_snake_case,
            to_camel_case,
            to_lower_camel_case,
        ]
    ]

    outp = replace_all(inp, mapping)

    print(outp, end="")


def cli_main() -> None:
    typer.run(main)


if __name__ == "__main__":
    cli_main()
