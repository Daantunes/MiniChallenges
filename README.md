# A) FIND THE BIGGEST SQUARE IN A DOTMATRIX

The doxmatrix is a matrix of zeros and ones. This algorithm can read a dotmatrix and return the length of the biggest square.

### Input
Several lines of zeros and ones that compose a squared matrix.

#### Example:
```
011100
001100
010111
000111
000110
011110
```
### Output
A number that represents the length of the biggest square.

#### Example:
```
2
```

# B) CREATE CYPHER

This cypher uses a chosen keyword to cypher a message. 
First the letters are selected and changed to uppercase. 
All the letters are disposed in columns under the letters of the keyword.
The columns are sorted by the alphabetical order of the keyword (if some letters are repeated, the order left-to-right is preserved).
Lastly, the columns are concatenated.

### Input
A set of lines, the first one represents the keyword.

#### Example:
```
WRITER
Hello, the quick brown fox jumped
over the lazy dog!
```
### Cypher
```
W R I T E R

H E L L O T
H E Q U I C
K B R O W N
F O X J U M
P E D O V E
R T H E L A
Z Y D O G
```
```
E I R R T W

O L E T L H
I Q E C U H
W R B N O K
U X O M J F
V D E E O P
L H T A E R
G D Y   O Z
```
### Output

The output is disposed in 8 blocks of 5 letters.

#### Example:
```
OIWUV LGLQR XDHDE TECBN OMEET AYLUO JOEOH HKFPR
Z
```
# C) Binary Tree

In the binary tree any left sub-tree has numbers less than or equal to the value of the root, and any right tree has numbers greater than the value of the root. 
This algorithm reads the preorder transversal and prints the post-order transversal.

## Preorder Traversal

- The root
- Recursive visit the left sub-tree
- Recursive visit the right sub-tree

## Post-order Traversal

- Recursive visit the left sub-tree
- Recursive visit the right sub-tree
- The root


### Input
A line of integers separated by a space that represents the preorder transversal.

#### Example:
```
7 3 1 4 7 10 8 9 13 11
```
### Representation of the tree
```
	       7                
	     /   \              
	    /     \             
	   /       \            
	  3        10           
	 / \     /    \         
	1   4   8     13        
	     \   \    /         
	      7   9  11         
```
### Output
A line of integers separated by a space that represents the post-order transversal.

#### Example:
```
1 7 4 3 9 8 11 13 10 7
```