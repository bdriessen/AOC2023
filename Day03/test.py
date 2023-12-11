from icecream import ic

# Create a list of dictionaries
dict1 = {'name': 'John', 'age': 7, 'class': 'First'}
dict2 = {'name': 'Merry', 'age': 8, 'class': 'Second'}
dict3 = {'name': 'Mark', 'age': 9, 'class': 'Third'}

dictlist = [dict1, dict2]
ic(dictlist)
dictlist.append(dict3)
ic(dictlist)

ic(dictlist[-1])

