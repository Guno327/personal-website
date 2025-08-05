## Assignment Description

**Important grading note: You must solve this problem without using any library
methods that your programming language provides for greatest common divisor,
modular exponentiation, modular multiplicative inverse, primality testing, or
RSA key generation.**\
\
Each line of input poses a question from number theory; your program must print
the answer, as detailed below.\
\
Input:

- gcd($$a$$
  , $$b$$
  ), where $$a\gt 0$$
  and $$b\gt 0$$
- exp($$x$$
  , $$y$$
  , $$N$$
  ), where $$N\gt 1$$
- inverse($$a$$
  , $$N$$
  ), where $$N\gt a\gt 0$$
- isprime($$p$$
  ), where $$p\gt 5$$
- key($$p$$
  , $$q$$
  ), where $$p$$
  and $$q$$
  are prime and $$p\neq q$$

\
Output:

- gcd($$a$$
  , $$b$$
  ): Print the greatest common divisor of $$a$$
  and $$b$$
  .
- exp($$x$$
  , $$y$$
  , $$N$$
  ): Print $$x^y$$
  mod $$N$$
  , which must be non-negative and less that $$N$$
  .
- inverse($$a$$
  , $$N$$
  ): Print $$a^{-1}$$
  (mod $$N$$
  \), which must be positive and less than $$N$$
  . If the inverse does not exist, print "none".
- isprime($$p$$
  ): Print "yes" if $$p$$
  passes the Fermat test for $$a=2$$
  ,$$a=3$$
  ,$$a=5$$
  ; Print "no" otherwise.
- key($$p$$
  , $$q$$
  ): print the modulus, public exponent, and private exponent of the RSA key
  pair derived from $$p$$
  and $$q$$
  . The public exponent must be the smallest positive integer that works; $$q$$
  must be positive and less than $$N$$
  .

## Example

### Input

    gcd 6 15
    gcd 2 13
    exp 6 5 7
    inverse 7 13
    inverse 6 9
    isprime 13
    isprime 10
    key 2 7
    key 5 3

### Output

    3
    1
    6
    2
    none
    yes
    no
    14 5 5
    15 3 3

## Code

[download](/static/file/number_theroy.py)
