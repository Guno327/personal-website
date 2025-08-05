## Assignment Description

Your boss, Mr. Anaga, is a constructor of word puzzles who is always giving you
unusual problems to solve. Today he has given you a list of words and asked you
to determine how many of the words are not anagrams of any other words on the
list.

For example, suppose that the list he gives you is

    me
    em
    to

You would need to tell him “1”, because “me” and “em” are anagrams of one
another, leaving only “to”. Or suppose that the list he gives you is

    tape
    rate
    seat
    pate
    east
    pest

You would need to tell him “2”, because “tape”/“pate” and “seat”/“east” are
anagrams, leaving only “rate” and “pest”.

## Example

### Input

    6 4
    tape
    rate
    seat
    pate
    east
    pest

### Output

    2

## Code

[download](/static/file/anagram.py)
