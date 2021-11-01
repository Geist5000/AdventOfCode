# AdventOfCode

To get the challenge click [here](https://adventofcode.com/2018/day/2)

# Contents
  - first.py: code for the first part of the challenge
  - second.py: code for the second part of the challenge
  - data.txt: challenge input
  - testInput.txt: usually the challenge input used in the example of the challenge (used for developing the code because the result is known)



## Idea:

input: abcde,fghij,klmno,pqrst,fguij,axcye,wvxyz
Iterate over each word, and over each character  
While Iterating over each character add the character to a tree structure. The depth of the node does describe which index the character in the word did have.  
If a character didn't exist check if any children combination of any subtree of the current depth could form the remaining of the current word. It this is true, the word is found. If false add remaining characters of current word into the tree structure
