
"""   Association Rule Mining   """

import pandas as pd

print('\n')
print(' '*23 + 'Apriori algorithm for Association Rule Mining')

print('\n')

df = pd.read_csv('C:/Users/ASHOK/Desktop/Nirma University/semester-6/Data Mining/practicals/prac 6/Market items.csv', header = None)

num = len(df)   # total number of data samples in the dataset

min_sup_perc = float(input('-> Enter the minimum support %: '))

min_sup_count = round((min_sup_perc * num) / 100)


min_conf_perc = float(input('-> Enter the minimum confidence %: '))

min_conf = round((min_conf_perc / 100), 6)

print('\n')

print('-> Minimum support count = %d' %min_sup_count)
print('')

print('-> Minimum confidence = %f' %min_conf)
print('')

print('')

# accessing an element of a dataframe by row index and column index 
# print(df.values[4, 2])

# converting a dataframe row to list
# li = list(df.loc[4])

# to get the number of rows (data samples) in a dataframe
# print(len(df))


"""  finding out all the unique items in the entire dataset  """

# function for union-operation on lists

def Union(list1, list2):
    UnionList = list1
    for elem in list2:
        if elem not in list1:
            UnionList.append(elem)
            
    return UnionList


# converting the dataframe into a list of lists (of data sample tuples)

ListOfTransactions = []

for i in range(0, num):
    li = list(df.loc[i])
    ListOfTransactions.append(li)
    
    
# total values = 150020
# 'NaN' (Not a Number) values = 120657

"""  Therefore, total number of items in all the transactions = 29,363  """

    
# all the unique items

ListOfAllItems = []

for li in ListOfTransactions:
    ListOfAllItems = Union(ListOfAllItems, li)
    

# nan = float('NaN')

ListOfItems = []

for item in ListOfAllItems:
    if pd.isnull(item) == False:
        ListOfItems.append(item)

# 'NaN' values have been handled

uniq = len(ListOfItems)


print('-> The set of all unique items in the dataset:')
print('')

print(ListOfItems)

print('\n')

print('-> The number of unique items: %d' %uniq)

print('\n')

"""  finding out the frequencies of each of these unique items  """

FrequencyDict = {}

FrequencyList = []

for item in ListOfItems:
    count = 0
    for li in ListOfTransactions:
        count = count + li.count(item)
    FrequencyDict[item] = count
    FrequencyList.append(count)


print('-> Frequency dictionary of all the dataset items:')
print('')
    
print(FrequencyDict)

print('\n')


"""   frequent 1-itemset   """

freq_1_itemset = []

freq_1_itemset_frequencies = []

for item in ListOfItems:
    if FrequencyDict[item] >= min_sup_count:
        freq_1_itemset.append(item)
        freq_1_itemset_frequencies.append(FrequencyDict[item])
    else:
        FrequencyDict.pop(item)


num_freq_1_itemset = len(freq_1_itemset)
        
print('-> frequent 1-itemsets:-')
print('')

print(freq_1_itemset)
print('\n')

print('-> Frequency dictionary of frequent 1-itemsets:-')
print('')

print(FrequencyDict)
print('\n')


"""   frequent 2-itemset   """

# combining frequent 1-itemsets to get 2-itemsets

all_2_itemset = []

for i in range(0, num_freq_1_itemset):
    for j in range(i+1, num_freq_1_itemset):
        if j == num_freq_1_itemset:
            break
        else:
            elem1 = freq_1_itemset[i]
            elem2 = freq_1_itemset[j]
            all_2_itemset.append([elem1, elem2])
            

print('-> List of all 2-itemsets:-')
print('')

print(all_2_itemset)

print('\n')

# finding frequent 2-itemsets

freq_2_itemset_dict = {}

freq_2_itemset = []

freq_2_itemset_frequencies = []

for TwoItemset in all_2_itemset:
    count = 0
    for transaction in ListOfTransactions:
        if TwoItemset[0] in transaction and TwoItemset[1] in transaction:
            count = count + 1
    if count >= min_sup_count:
        key = TwoItemset[0] + ', ' + TwoItemset[1]
        freq_2_itemset_dict[key] = count
        freq_2_itemset.append(TwoItemset)
        freq_2_itemset_frequencies.append(count)
        

print('-> frequent 2-itemsets:-')
print('')

print(freq_2_itemset)
print('\n')

print('-> Frequency dictionary of frequent 2-itemsets:-')
print('')

print(freq_2_itemset_dict)
print('\n')


"""   Association Rules   """
    
print(' '*40 + 'Association Rules')
print('\n')

print('-> Number of frequent 1-itemsets = %d' %len(freq_1_itemset))
print('')

print('-> Number of frequent 2-itemsets = %d' %len(freq_2_itemset))
print('\n')


def Association_1_itemset_to_1_itemset(TwoItemset):
    item1 = TwoItemset[0]   # item a
    item2 = TwoItemset[1]   # item b
    
    # a two-way association determining function, from TwoItemset [a, b]
    # i.e., examines 'a -> b' as well as 'b -> a'
    
    rule1 = False
    rule2 = False
    
    """   'a -> b'   """
    
    freq_a = FrequencyDict[item1]
    
    freq_a_and_b = 0
    
    for transaction in ListOfTransactions:
        if item1 in transaction and item2 in transaction:
            freq_a_and_b = freq_a_and_b + 1
            
    conf_a_implies_b = round((freq_a_and_b / freq_a), 6)
    
    if conf_a_implies_b >= min_conf:
        rule1 = True
        
    """   'b -> a'   """
    
    freq_b = FrequencyDict[item2]
    
    conf_b_implies_a = round((freq_a_and_b / freq_b), 6)
    
    if conf_b_implies_a >= min_conf:
        rule2 = True
        
    
    RuleList = []
    
    if rule1 == True:
        RuleList.append(item1 + ' -> ' + item2)
        
    if rule2 == True:
        RuleList.append(item2 + ' -> ' + item1)
        
    return RuleList



RuleListFor_1_itemset_to_1_itemset_Association = []

for TwoItemset in all_2_itemset:
    rule = Association_1_itemset_to_1_itemset(TwoItemset)
    RuleListFor_1_itemset_to_1_itemset_Association = RuleListFor_1_itemset_to_1_itemset_Association + rule
    

print('# List of rules for 1-itemset to 1-itemset association:-')
print('')

print(RuleListFor_1_itemset_to_1_itemset_Association)
print('\n')

print('# List format:-')
print('')

for rule in RuleListFor_1_itemset_to_1_itemset_Association:
    print(rule)

print('\n')


    
    
    
    







