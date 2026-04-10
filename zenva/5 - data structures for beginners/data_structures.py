
def RunLists():
    list = [0,1,2,3,4,5,6]
    print("list>" + str(list))

    slicedList = list[2:5] # slicing a list from index 2 to index 4 (5 is exclusive)
    print("sliced list>" + str(slicedList))

    list[2:5] = [8,9] # replacing the elements from index 2 to index 4 with new values
    print("replaced element in list>" + str(list))

    list.append(7) # adding an element to the end of the list
    print("append element in list>" + str(list))

    list.extend([8,9]) # adding multiple elements to the end of the list
    print("extend list in list>" + str(list))

    list.remove(8) # removing the first occurrence of the value 8 from the list
    print("remove element (first of its kind)from list>" + str(list))

    poppedElement = list.pop(2) # removing the element at index 2 from the list
    print("pop element at index 2 from list>" + str(list) + " (popped element: " + str(poppedElement) + ")")

    list.sort() # sorting the list in ascending order

    print ("what about sorting ?" + str(list))

    list.reverse() # reversing the order of the list

    print ("what about reversing ?" + str(list))

def RunLoops():
    loopedList = [0,1,2,3,4,5]

    for n in loopedList:
        print("looping through list>" + str(n))

    print("10 in list ?>" + str(10 in loopedList)) # checking if 10 is in the list (returns False)

    print("only numbers > 3 ?" + str([n for n in loopedList if n > 3])) # using list comprehension to filter elements greater than 3

    print("applying function to each element in list>" + str([double(n) for n in loopedList])) # using list comprehension to apply a function (doubling) to each element in the list

def double(integer):
    return integer * 2

def runStrings():
    string = 'this is a string'
    print("first element of string ?> " + string[0] + "(" + string + ")") # accessing the first character of the string
    print("sliced string> " + string[5:7]) # slicing the string
    print("want to find first index on 's' in string ?> " + str(string.index('s'))) # finding the first index of the character 's' in the string
    print("want to replace 'string' with 'text' in string ?> " + string.replace('string', 'text')) # replacing a substring in the string

def runDictionaries():
    dictionary = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    print("dictionary> " + str(dictionary)) # printing the dictionary

    print("accessing value by key 'name' > " + dictionary['name']) # accessing a value by its key

    dictionary['age'] = 31 # updating the value associated with the key 'age'
    print("updated age in dictionary> " + str(dictionary))

    dictionary['country'] = 'USA' # adding a new key-value pair to the dictionary
    print("added country to dictionary> " + str(dictionary))

    del dictionary['city'] # removing a key-value pair from the dictionary
    print("removed city from dictionary> " + str(dictionary))

    dictionary['occupation'] = 'Engineer' # adding another key-value pair to the dictionary
    print("added occupation to dictionary> " + str(dictionary))

    print("keys in dictionary> " + str(dictionary.keys())) # printing all the keys in the dictionary

    print("trying to get a value for a non-existent key 'hobby' with get method> " + str(dictionary.get('hobby', 'Not Found'))) # trying to get a value for a non-existent key

    popedValue = dictionary.pop('age') # removing a key-value pair and getting the value
    print("popped age from dictionary> " + str(dictionary) + " (popped value: " + str(popedValue) + ")")

    for key, value in dictionary.items(): # iterating through the dictionary items
        print("key: " + key + ", value: " + str(value))

    newdict = {key.upper(): value for key, value in dictionary.items()} # using dictionary comprehension to create a new dictionary with uppercase keys
    print("dictionary with uppercase keys> " + str(newdict))

def runTuples():
    tuple = (0,1,2,3,4,5)
    print("tuple> " + str(tuple)) # printing the tuple

    print("first element of tuple > " + str(tuple[0])) # accessing the first element of the tuple

    slicedTuple = tuple[2:5] # slicing the tuple from index 2 to index 4 (5 is exclusive)
    print("sliced tuple> " + str(slicedTuple))

    print("want to find first index on '3' in tuple > " + str(tuple.index(3))) # finding the first index of the value 3 in the tuple

    number, string, float = tuple_packing() # unpacking a tuple into separate variables
    print("unpacked tuple> number: " + str(number) + ", string: " + string + ", float: " + str(float))

def tuple_packing():
    return (1, 'hello', 3.14) # returning a tuple with different types of elements

def runSets():
    set = {0,1,2,3,4,5}
    print("set> " + str(set)) # printing the set

    set.add(6) # adding an element to the set
    print("added element to set> " + str(set))

    set.update([7,8]) # adding multiple elements to the set
    print("updated set with multiple elements> " + str(set))

    set.remove(8) # removing an element from the set
    print("removed element from set> " + str(set))

    print("is 3 in set? > " + str(3 in set)) # checking if an element is in the set (returns True)

    newSet = {4,5,6,7,8,9}
    print ("new set> " + str(newSet)) # printing the new set

    print("intersection of sets> " + str(set & newSet)) # finding the intersection of two sets
    print("union of sets> " + str(set | newSet)) # finding the union of two sets
    print("difference of sets> " + str(set - newSet)) # finding the difference of two sets

def runChallenge(list):
    # challenge: write a function that takes a list and outputs
    # a list of tuples that contain each unique element of the list
    # alongside the number of tumes that element appears in the list
    elements = {}
    [updateDictionary(elements, n) for n in list]
    return [(key, value) for key, value in elements.items()]

def updateDictionary(dictionary, key):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1
    

## lists
RunLists()

## loops
RunLoops()

## strings: immutable sequence of characters
runStrings()

## dictionaries: collection of key-value pairs
runDictionaries()

## tuples: immutable collection of values
runTuples()

## sets: collection of unique values
runSets()

## run challenge
print(runChallenge([1,2,2,3,4,4,5,1]))