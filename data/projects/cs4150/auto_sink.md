## Assignment Description

I am traveling next month to the beautiful country of Dagonia, where I am going
to rent a car. As I have been making my plans, I have learned four interesting
facts about the Dagonian highway system:

- The highways lead from city to city; they do not intersect anywhere else.
- Each highway is for travel in one direction only.
- The highway system is acyclic; once you drive away from a city, there is no
  way to legally drive back.
- Every city charges a toll, payable when you enter the city via a highway.

\
There are a number of driving trips I would like to take while in Dagonia, and
for each I need to determine whether the trip is possible and, if so, the
minimum amount I will need to pay in tolls.\
\
For example, Figure 1 is a map of the mining district of Dagistan. If I want to
drive from Sourceville to SinkCity, the minimum toll will be $25 ($15 for
entering Weston and $10 for entering SinkCity). If I want to drive from Easton
to Easton, the minimum toll is $0 (since I am already there). If I want to drive
from SinkCity to Weston, I’m out of luck.\
![image](/static/img/ps4.png)\
\
Given a map of a portion of the Dagonian highway system and a list of trips I
would like to take, your job is to tell me, for each trip, what the minimum toll
would be (if the trip is possible) or “NO” (otherwise).

## Example

### Input

    4
    Sourceville 5
    SinkCity 10
    Easton 20
    Weston 15
    4
    Sourceville Easton
    Sourceville Weston
    Weston SinkCity
    Easton SinkCity
    6
    Sourceville SinkCity
    Easton SinkCity
    SinkCity SinkCity
    Weston Weston
    Weston Sourceville
    SinkCity Sourceville

### Output

    25
    10
    0
    0
    NO
    NO

## Code

[download](/static/file/auto_sink.py)
