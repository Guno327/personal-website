## Assignment Description

At the Benjamin Franklin School in Broken Fork Saskatchewan, the spreading of
rumors is strictly regulated.\
\
On Day 0, a student wishing to spread a rumor must notify the school office. No
spreading of the rumor may occur that day.\
\
On Day 1, the student must tell all of his or her friends the rumor before the
end of the day. (Leaving out any friends causes hurt feelings, so this rule is
strictly enforced.) No further spreading of the rumor is allowed that day.\
\
On Day 2, each student who learned of the rumor the previous day must pass the
rumor along to every friend who has not yet heard the rumor. No further
spreading of the rumor is allowed that day.\
\
The rumor must continue spreading in this fashion until the day comes that no
more spreading of the rumor is possible under the rules. On that day, the school
principal reads the rumor over the intercom, which guarantees that all students
have heard the rumor.\
\
Following the intercom announcement, the principal must file a report with the
school board. In the report, the principal must list the student who started the
rumor, followed by the students (in lexicographic order) who first learned of
the rumor on Day 1, and so on, ending with the students (in lexicographic order)
who first learned of the rumor over the intercom.\
\
For example, suppose the student body consists of Cam, Art, Edy, Bea, and Dan,
where Bea and Edy are friends, Dan and Bea are friends, and Art and Dan are
friends.

- On Day 0, Dan notifies the office of his plan to start a rumor about the
  school lunches.
- On Day 1, Dan spreads the rumor to his two friends, Bea and Art.
- On Day 2, Bea tells her friend Edy. Bea’s other friend (Dan) already knows the
  rumor, as does Art’s only friend (also Dan).
- On Day 3, the rules don’t permit anyone else to be told the rumor, since Edy’s
  only friend (Bea) already knows. The principal reads the rumor over the
  intercom and invites everyone to lunch at McDonalds. Cam, who is new to the
  school and has no friends, finally learns what everyone else has been
  whispering about.

\
After lunch, the principal fires the lunchroom staff and files the rumor report,
listing the students in this order: Dan, Art, Bea, Edy, Cam.\
\
Your job is to help the principal prepare rumor reports.

## Example

### Input

    5
    Cam
    Art
    Edy
    Bea
    Dan
    3
    Bea Edy
    Dan Bea
    Art Dan
    2
    Dan
    Cam

### Output

    Dan Art Bea Edy Cam
    Cam Art Bea Dan Edy

## Code

[download](/static/file/rumor_mill.py)
