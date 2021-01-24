# AdventOfCode

To get the challenge click [here](https://adventofcode.com/2020/day/13)

# Notes

input: 4x6

finde ersten Index für 4 index 0 und 6 index 2

match: 6

nächstes match ist (match wenn 6*x-2 = 4*y):

6%4=2

1*6 = 6     (match 1*4 = 4)

2*6 = 12    (kein match)

3*6 = 18    (match) (4*4 = 16)

4*6 = 24    (kein match)

5*6 = 30    (match 6*4 = 28)

6*6 = 36    (kein match)

7*6 = 42    (match 10*4 = 40)

8*6 = 48    (kein match)

9*6 = 54    (match 13*4 = 52)

10 * 6 = 60 (kein match)

11 * 6 = 66 (match 16*4 = 64)

diff der matches = 12

gleicher ablauf mit 4x15:

Matches (15*x-2 = 4*y):

15%4=3

1*15 = 15   (kein match)

2*15 = 30   (match 7*4 = 28)

3*15 = 45   (kein match)

4*15 = 60   (kein match)

5*15 = 75   (kein match)

6*15 = 90   (match 22*4 = 88)

7*15 = 105  (kein match)

8*15 = 120  (kein match)

9*15 = 135  (kein match)

10*15 = 150 (match 37*4 = 148)

11*15 = 165 (kein match)

12*15 = 180 (kein match)

13*15 = 195 (kein match)

14*15 = 210 (match 52*4=208)

diff der matches = 60

gleicher ablauf mit 11x15:

Matches (15*x-2 = 11*y || (15*x-2)%11 = 0):

15%11=4


1*15=15         (kein match)
2*15=30         (kein match)
3*15=45         (kein match)
4*15=60         (kein match)
5*15=75         (kein match)
6*15=90         (match 8*11=88)
7*15=105        (kein match)
8*15=120        (kein match)
9*15=135        (kein match)
10*15=150       (kein match)
11*15=165       (kein match)
12*15=180       (kein match)
13*15=195       (kein match)
14*15=210       (kein match)
15*15=225       (kein match)
16*15=240       (kein match)
17*15=255       (match 23*11=253)
18*15=270       (kein match)
19*15=285       (kein match)
20*15=300       (kein match)

diff der matches = 165

Frage: wie kann ich das match vervielfachen um auf die nächste valide zahl zu kommen