# Dictionary theory

## Creating a Dictionary
```python
my_dict = {'a':1,'b':2}
```

## Inserting an element in the dictionary
```python
mydict['c'] = 3
```

## Updating an element in a dictionary
```python
mydict['a'] = 0
```

## Deleting an element from dictionary

### Method:1
#### pop()
In this method we have to give the key as input and it will delete the key and value pair from the dictionary and return the value
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
print(mydict.pop('a'))
# output: 0
print(mydict)
# output: {'b': 2, 'c': 3, 'd': 4}

```
### Method:2
#### popitem()
This method will delete arbitary items, both key and value and returns both the values
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
print(mydict.popitem())
# output: ('d', 4)
print(mydict)
# output: {'a': 0, 'b': 2, 'c': 3}

```
### Method:3
#### Clear()
This method will delete whole dictionary
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
mydict.clear()
print(mydict)
# output: {}

```
### Method:4
#### del
With this method we need to input value of key and the key value pair will be deleted
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
# The way we write this function is different then other 3 functions
del mydict['a']
print(mydict)
# output: {'b': 2, 'c': 3, 'd': 4}
# we can delete whole dictiionary using this function
del mydict

```
## Dictionary Methods
### Copying the Dictionary
`.copy()` is used to copy a dict into new dict and we can then use new dict without updating old one
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
newdict = mydict.copy()
newdict['e'] = 5
print("original dictionary:", mydict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4}
print("copied updated dictionary:", newdict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

```
### Creating a Dictionary from keys
`fromkeys` method is used for that. In input it will take a sequence, which will be keys, and a value dictionary.`fromkeys(sequence,value)`
```python

keys = ['a','b','c','d','e']
value = 100
newdict = {}.fromkeys(keys,value)
print(newdict)
# output: {'a': 100, 'b': 100, 'c': 100, 'd': 100, 'e': 100}

```
### Get Method
`.get(key,value)`. If the key is present the output will be the corresponding value. If key is not present the output, the value will become default value and it will be returned
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
print("value corresponding to the key 'a' in dict:", mydict.get('a',100))
# output: 0
print("output when key is not present but default value is specified '100':", mydict.get('r',100))
# output: 100
print("output when key is not present and default value is not specified:", mydict.get('r'))
# output: None
# value in mydict is not updated 
print(mydict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4}

```
### .items Method
`.items()`. This function will return a list of all key value pairs in dictionary in the form of tuples
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
print(mydict.items())
# output: dict_items([('a', 0), ('b', 2), ('c', 3), ('d', 4)])

```
### Get Keys and Values Method
`.keys()`. To get a list of all the keys
```python 

mydict = {'a':0,'b':2,'c':3,'d':4}
print("Dictionary:", mydict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4}
print("Keys:", mydict.keys())
# output: dict_keys(['a', 'b', 'c', 'd'])

```
`.values()`. To get a list of all the values
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
print("Values:", mydict.values())
# output: dict_values([0, 2, 3, 4])

```
### `Setdefault()` Method
`setdefault(key,default_value)`.It will return the value of key if the key is present.If the key is not present it will update the dictionary with the assigned key and value
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
print("Value of the key 'a':",mydict.setdefault('a',5))
# output: 0
print("Added key 'e' and returned its value '5':", mydict.setdefault('e',5))
# output: 5
print("Updated dictionary:", mydict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Added key 'f' and returned none as its value is not specified:", mydict.setdefault('f'))
# output: None
print("new updated dict:", mydict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': None}

```
### `Update()` Method
`dictionary.update(other_dictionary)` OR `dictionary.update(tuple)`
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
newdict = {'e':5,'f':6,'g':7,'h':8}
tuple_values = (('i',9),('j',10),('k',11),('l',12))
mydict.update(newdict)
print("updated mydict:", mydict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
# OR
mydict.update(tuple_values)
print("updated mydict:", mydict)
# output: {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'i': 9, 'j': 10, 'k': 11, 'l': 12}

```
## Dictionary Functions
### `in` function
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
k = 'a'
if k in mydict:
    print("yes")
# output: yes
# IN operator only reads keys and not values
l = 0
if l in mydict:
    print("no")
# no output
# To check value we need to call .values()
print(0 in mydict.values())
# output: True

```
### `for' Function
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
for keys in mydict:
    print(mydict[keys])
# output: 0
#         2
#         3
#         4

```
### `all()` Function
It returns true only if all the elements of the iterable are true else false. If the dictioanry is empty it will return true
```python

mydict = {'1':True,'2':True}
print(all(mydict))
# output: True
newdict = {}
print(all(newdict))
# output: True

```
### `any()` Function
This method will return true if any element of the collection is true orelse false. If there is an empty dictionary then it returns false
```python

mydict = {'1':True,'2':False}
print(any(mydict))
# output: True
newdict = {}
print(any(newdict))
# output: False

```
### `len()` Function
It gives the number of key value pairs of dictionary
```python

mydict = {'a':0,'b':2,'c':3,'d':4}
print(len(mydict))
# output: 4

```
### `sorted()` Function
It sorts the dict according to key
```python

mydict = {'d':5,'e':2,'a':0,'b':4}
print(sorted(mydict))
# output: ['a', 'b', 'd', 'e']
newdict = {'buubuininijijd':5,'afae':2,'wfwwa':0,'bfefawf':4}
print(sorted(newdict,key=len)) # it will sort based on the length of the key
# output: ['afae', 'wfwwa', 'bfefawf', 'buubuininijijd']

```