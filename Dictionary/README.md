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
#output: {'b': 2, 'c': 3, 'd': 4}
```