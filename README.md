# cawspr

Case And Word Separation Preserving Replace (CAWSPR)

## What does this do?

This script is as simple as it is stupid: You give it a list of words to
replace (e.g. `hello world`) and a list of words to replace them with (e.g.
`goodbye world`) and it will perform this replacement for various compositions
of these words that are common e.g. in programming:

- separated by spaces: `hello world` → `goodbye world`
- lowercase and separated by underscores (snake_case):
  `hello_world` → `goodbye_world`
- uppercase and separated by underscores (SCREAMING_SNAKE_CASE):
  `HELLO_WORLD` → `GOODBYE_WORLD`
- lowercase and separated by hyphens (kebab-case):
  `hello-world` → `goodbye-world`
- separated only by capitalizing the first letter of each word (CamelCase):
  `HelloWorld` → `GoodbyeWorld`
- separated only by capitalizing the first letter of each word except the first
  (lowerCamelCase):
  `helloWorld` → `goodbyeWorld`

The text in which to make these replacements must be piped into the script's
standard input and it will output the resulting modified text to standard
output.

That's it.

## Installation

```bash
pip3 install git+https://gitlab.com/smheidrich/cawspr.git
```

## Usage

Replacing all occurrences of `hello world` and its variants in a file
`original.txt` with `goodbye world` and writing the result to `replaced.txt`:

```bash
cat original.txt | cawspr 'hello world' 'goodbye world' > replaced.txt
```

## Advertisement

Want to perform such replacements for both file contents *and* file paths in a
directory recursively? Consider
[full-apply](https://gitlab.com/smheidrich/full-apply) which works great with
cawspr!

## Similar projects and other resources

- [Softwarerecs StackExchange
  question](https://softwarerecs.stackexchange.com/q/84786/13721) in which I
  asked if anyone knows of an existing CLI tool that does this (perhaps more
  will crop up in the future)
- The answers to [this StackOverflow question] are full of links to vim plugins
  for the same purpose (but I wanted it as a CLI tool):
  - [abolish.vim](https://github.com/tpope/vim-abolish) (can do this and other
    loosely related things)
  - [SmartCase](https://www.vim.org/scripts/script.php?script_id=1359)
  - [keepcase.vim](https://www.vim.org/scripts/script.php?script_id=6)
