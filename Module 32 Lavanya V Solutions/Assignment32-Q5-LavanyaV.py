# maximum times of a no
# can ba handled using hastable- by creating a dictionary


class myHashTable:
    def __init__(self):
        self.hashTable = dict()

    def put(self, key, data):
        self.hashTable[key] = data

    def remove(self, key):
        self.hashTable.pop(key)

    def remove_last_item(self):
        self.hashTable.popitem()

    def delete_item(self, key):
        del self.hashTable[key]

    def display(self):
        print(self.hashTable)

    def get(self, key):
        return self.hashTable[key]


# function to calculate maximum occurrance


def max_occ(arr):
    # creating a hashtable
    hash1 = myHashTable()
    for i in arr:
        if i in hash1.hashTable.keys():
            hash1.put(i, hash1.hashTable[i] + 1)
        else:
            hash1.put(i, 1)
    hash1.display()
    keysInHash = hash1.hashTable.keys()
    largest = 0
    for each in keysInHash:
        if hash1.get(each) > largest:
            largest = hash1.get(each)
            largestNo = each
    return largestNo


n = int(input("Enter the no of test cases  "))
for i in range(n):
    no = [int(x) for x in input("Enter the nos ").split()]
    print(max_occ(no))
