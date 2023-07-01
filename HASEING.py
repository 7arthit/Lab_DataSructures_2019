def display_hash(hashTable):
	for i in range(len(hashTable)):
		print(i, end = " ")
		for j in hashTable[i]:
			print("-->", end = " ")
			print(j, end = " ")
		print()
HashTable = [[] for _ in range(7)]
def Hashing(keyvalue):
	return keyvalue % len(HashTable)
def insert(Hashtable, keyvalue, value):
	hash_key = Hashing(keyvalue)
	Hashtable[hash_key].append(value)
insert(HashTable, 30, 'cat')
insert(HashTable, 42, 'rat')
insert(HashTable, 51, 'bat')
insert(HashTable, 14, 'toy')
insert(HashTable, 12, 'man')
insert(HashTable, 3,  'big')
insert(HashTable, 7,  'boy')
insert(HashTable, 17, 'zoo')
display_hash (HashTable)