## Assignment Description

Nils and Mikael are intergalaxial fighters as well as lethal enemies. Now Nils
has managed to capture the poor Mikael in his dark dungeons, and it is up to you
to help Mikael escape with as much of his pride intact as possible.\
\
The dungeons can be viewed as a set of corridors and intersections. Each
corridor joins two intersections. There are no guards, traps, or locked doors in
Nils’ dungeon. However, there is one obstacle which makes escaping from the
dungeon a perilious project: in each corridor there is a sentry, armed with a
factor weapon. (As is commonly known, a factor weapon with factor $$f$$

reduces the size of its target to a factor $$f$$

of its original size, e.g. if Mikael is $$8$$

gobs large and is hit by a factor weapon with factor $$f=0.25$$

his size will be reduced to $$2$$

gobs.)\
\
Mikael will not be able to pass through a corridor without being hit by the
factor weapon (but luckily enough, reloading the factor weapon takes enough time
that the sentry will only have time to shoot him once as he passes through). It
seems inevitable that Mikael will come out of this adventure a smaller man, but
since the sentries have different factors in their factor weapons, his final
size depends very much on the route he takes to the exit of the dungeons.
Naturally, he would like to lose as little size as possible, and has asked you
to help him accomplish that.

## Example

### Input

    3 3
    0 1 0.9
    1 2 0.9
    0 2 0.8
    2 1
    1 0 1
    0 0

### Output

    0.8100
    1.0000

## Code

[download](/static/file/get_shorty.py)
