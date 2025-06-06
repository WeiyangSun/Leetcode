"""
380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:
- RandomizedSet() initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when
this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

"""
Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""

import random # for getRandom function

class RandomizedSet:

    def __init__(self):
        self.randomizedset_dict = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.randomizedset_dict:
            return False # if value exists, insertion fails
        self.values.append(val)
        self.randomizedset_dict[val] = len(self.values) - 1 # map value to index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomizedset_dict:
            return False # if value doesn't exist, removal fails
        idx = self.randomizedset_dict[val]
        last_val = self.values[-1] # getting last value in list
        self.values[idx] = last_val # move last value to index of the value to remove
        self.randomizedset_dict[last_val] = idx # update index mapping
        self.values.pop()
        del self.randomizedset_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)