# Notes

Things to note: 

This uses **Sliding Window** algorithm

The way it works is to **save the index** of the last occurence of a given character in a string

So whenever you found a duplicate character, replace the start window index with the **(index of the character + 1)**

