# AdventOfCode

To get the challenge click [here](https://adventofcode.com/2018/day/2)

# Contents
  - first.py: code for the first part of the challenge
  - second.py: code for the second part of the challenge
  - data.txt: challenge input
  - testInput.txt: usually the challenge input used in the example of the challenge (used for developing the code because the result is known)


# Part Two


## Task

You get a list of words, find the two words which have a one character difference.

## Idea:
### Tree Stucture:
Each character of each already added word is inside the tree. If the character was the first character of the word, it is located at the depth of zero iside the tree.
A tree for the following three words would look like this:  
Words: uzhbn,azhbn,azhcn
``` 
           root
           / \
          u   a
         /     \
        z       z
       /         \
      h           h
     /           / \
    b           c   b
   /           /     \
  n           n       n
```

### Algorithm
Check if any child node is the first character of the current word. If a node exists, remove the first character fo the word. Repeat the process with the found node as root node. If no node exists, check if the remaining word (without the first character) is existing inside any subtree of the current tree.  
If a subtree exists, search is done. If no subtree contains the whole remaining word, add the current word to the tree, and continue search with next word.
