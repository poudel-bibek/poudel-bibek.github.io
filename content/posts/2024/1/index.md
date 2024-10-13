---
title: "Lessons on LeetCode: Part I"
date: 2024-10-12T20:00:00
draft: true
summary: "Sample article showcasing basic code syntax and formatting for HTML elements."
#showtoc: true
excludeFromBlog: false

cover:
    image: "images/lc.png"
    alt: "<alt text>"
    caption: "" 
    relative: false 
    hiddenInList: false
    hiddenInSingle: false
    hidden: false # Hidden from the home in the main config, but unhide here.
---

The meta lesson: learn patterns not problems.


Brute force:

- My go-to strategy has always been to loop through the two arrays. However, depending on the nature of the problem (where operations between (1, 2) and (2,1) is same), one simple trick is to start the second array from current position of the first array. i.e., perform the upper triangular comparision.

{{< figure src="images/1.png" attr="Photo by Aditya Telange on Unsplash" align=center link="https://unsplash.com/photos/Z0lL0okYjy0" target="_blank" >}}



```python {linenos=inline}
# delete an item from a list using index
a = [10, 12, 13, 14, 15]
del a[3] # deletes the item in index 3

# Interestingly the same method works to remove an item from dictionary based on key
mydict = {5: 3, 2: 1, 3: 3, 1: 2}
del mydict[5]
print(mydict)

# delete an item from a list using value
a = [10, 10, 12, 13, 14, 15]
a.remove(10)
```

```python {linenos=inline}
# Simple set operations
lista = [10, 12, 13, 14, 15, 14, 14]
seen = set()
for a in lista:
    if a in seen: # A set has a constant lookup time i.e., better than list here
    # How come a set has a constant lookup time O(1)
    # In Python, a set data structure is implemented using a hash table thats why
        print(f"Repeated: {a}")
    else: 
        seen.add(a)
```

```python {linenos=inline}  
# Dict get method with default return values
chars = "believers"
mydict= {}
for char in chars: 
	# If it finds, it returns the stored value. If not return a 0
	mydict[char] = mydict.get(char, 0) + 1 # Genius way to count chars in a string
print(mydict)
```

```python {linenos=inline}
# Pair of items using zip
ids = [1, 2, 3, 4]
for item in zip(ids, ids[1:]): # Karpathy Pythonic
    print(item) # Gets the pairs (1,2), (2,3), (3,4)
								# If its changed to ids[2:] we get (1,3), (2,4)
								
# Very helpful to traverse the upper triangle.
nums = [1, 2, 3, 4, 5]
for i in range(1, len(nums)):
    for item in zip(nums, nums[i:]):
        print(item)
```

```python {linenos=inline}
# Initializing an array of size
new_arr = [0] * size
```

```python {linenos=inline}
# I am habituated to think like a for loop, to convert for loop to while loop
for i in range(k): 

# To make this a while loop it requires initialization, update and termination
i = 0 
while i< k: 

	# somewhere inside  
	i+=1
	
What is the advantage of using a while loop over a for loop?
```
  
```python 
mydict = {1: 3, 2: 2, 3: 1}

#mydict.keys() is of dict_keys type and mydict.values() is of dict_values type
#need to make it a list explicitly with 

list(mydict.keys()), list(mydict.values())
```


```python
# You can also sort the words. In some cases this may be helpful (such as checking equality)

```

Lists are immutable but tuple is mutable if we do tuple() on the list, they become mutable.. thats why tuple exist in the python language.

```python
ord('a') returns the unicode of the alphabet. then you can do +1 to increment it.
then you can use chr() to convert it back to the word
```

```python
#Instead of using if and else, return the condition itself:  
return pattern_word == pattern
```

why do we need a ; after break? break;

Never assume.

Can I import things build into standard python package to solve leetcode?

```python
# A frequent pattern that emerges in many problems is to find top k elements. 
# An efficient way to do it is quickselect. 

```

```python
# Quicksort and Quickselect
```

- Does average case mean worst cases occur rarely in practice?

- Set and dict are unordered collections.

---

There are ways to know about things without creating the thing. For example to know the length of the longest sequence, you dont hav

```jsx
''.join()
```

Python tricks from Karpathy:
Karpathy codes like a wizard. 

```
zip window trick:
```

```
print(f'{log_likelihood=}')
log_likelihood=tensor(-38.7856)
```


