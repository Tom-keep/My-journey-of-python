import random
list = ['c++','python','c','java','go']
#print(list[-1:-3:-1])
print("----------------------------------------------------------------------")
#list operations
list.append('php')
print(list)#['c++', 'python', 'c', 'java', 'go', 'php']
list.insert(2,'rubyruby')
print(list)#['c++', 'python', 'rubyruby', 'c', 'java', 'go', 'php']
#print(list.remove('c'))#None this will remove the first occurrence of 'c' in the list and return None
list.remove('c')
print(list)#['c++', 'python', 'rubyruby', 'java', 'go', 'php']
print(list.pop())#'php' this will remove the last element and return it
list.pop()
print(list)#['c++', 'python', 'rubyruby', 'java', 'go']
list[2]='ruby'
print(list)#['c++', 'python', 'ruby', 'java', 'go']
print(list.index('ruby'))#2
list.sort()
print(list)#['c++', 'java', 'python', 'ruby', 'go']
print("----------------------------------------------------------------------")
list1=['c++','c++','c++']
list1.remove('c++')
print(list1)   #same remove the last element
print("----------------------------------------------------------------------")
list2 = [1,2,3,4,5]
list2_change = [i for i in list2 if i > 2]
print(list2_change)#[3, 4, 5]
print("----------------------------------------------------------------------")