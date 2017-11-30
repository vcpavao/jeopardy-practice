# jeopardy-practice

## Summary
Program that quizzes user with Jeopardy clues that have already
been parsed into a SQLite3 database (there are other repos that
perform this), and uses machine learning to track incorrect questions
and user progress. It has only been tested with Python 3.6.* and
SQLite3.10*

## Example Use

This program is run through Python console.

Answering a clue correctly will appear like the following:

```diff
- CATEGORY:  ('THE PIANIST',)
- Once the highest-paid musician, he dazzled us with costumes & candelabra, as well as his piano playing
+ Liberace
- Correct!
- 33.333333333333336 %
```

whereas answering one incorrectly will appear like this:

```diff
- CATEGORY:  ('A TEXTBOOK CATEGORY',)
- Michael Pacione's "Urban Geography" covers "urban" this, the design & regulation of populated spaces
+ demography
- ANSWER:  urban planning
- 20.0 %
```
