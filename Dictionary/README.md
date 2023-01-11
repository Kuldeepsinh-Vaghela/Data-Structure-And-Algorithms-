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