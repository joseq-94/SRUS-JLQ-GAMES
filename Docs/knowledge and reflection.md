# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> all of the hash function take a key(UID) and transform it into an integer.
> then, we use this hash value to generate a index within the hash table
> this index is used to store the player in one player list.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> For the SSH and the Sum of ASCII functions, some qualities such as uniformity, collision
resistance, sensitive and security are very poor or nonexistent. however, both functions are
efficient and fully deterministic.

>The pearson hash and the pyhon built-in hash perform much better in every area but its main
weakness is security due to they are not designed to be cryptographically.

>Finally, SHA256 hash function performs strongly in all areas, including security due to its
cryptographic design and its only disadvantage is lower efficiency, since the hashing process is
 more computationally.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> for me, the three most important attribute of a hash function are uniformity because a 
> hash map relies on an even distribution of keys across the tables, determinism because the 
> same key must always map to the same index, and efficiency because the hash function are 
> executed on every insertion, lookup and deletion.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I choose the pearson hash for this task because it has a strong balance between the 
> attributes, this function can create more distribution and reduce the collisions

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> the function is using a loop to iterate through each character and get numbers from UID and 
> then mapping the result through different tables. this contributes to uniformity, 
> determinism and efficiency

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> function insert player
> key = player.uid
> index = hash_function(key)
> self.hash_table[index].append(player)
> increase size +1

## Reflection

1. What was the most challenging aspect of this task?

> The most challenging aspect was implementing the unittest for the playlist deletion logic. 
> the list occasionally raised errors because the delete_key method to access prev on a none 
> node. this happens when the head is deleted or the list is empty. so I use a conditional 
> logic to correctly handle.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> if the number of player were small, I would replace the playerlist with a simple python list 
> because I do not need to use the pointer-management complexity of a doubly linked list and 
> avoid possible bugs.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.