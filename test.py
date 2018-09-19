# def testFunc(*ints):
#     sum = 0
#     for num in ints:
#         sum += num
#         #print(num)
#     return sum
# a = testFunc(8,9,6,2,9,7,5,8)
# #a = testFunc(1,3,6)
#
# print(a)

# def testFunc1(name, *score, **option):
#     """tqweqweqweqweqwe"""
#     print(name)
#     sum = 0
#     for s in score:
#         sum += s
#     print("총점 : ", sum)
#     if (option['avg'] == True):
#         print("평균 : ", sum/len(score))
#
#
# testFunc1("qwewqe",90,90,20,20, avg=True)
#
# help(testFunc1)


# a = [n for n in range(1,11)]
# print(a)
# def half(s):
#     return s/2
#
# score = [46, 23, 11, 98, 20]
#
# for s in map(half, score):
#     print(s)
#

# score = [45, 89, 72, 53, 95]
# for s in filter(lambda x:x < 60, score):
#     print(s)

# score = [45, 89, 72, 53, 94]
#
# for s in map(lambda x:x / 2, score):
#     print(s)

# list1 = [1,2,3]
# list2 = list1.copy()
# list2[1] = 4
# print(list1)
# print(list2)
import copy
list0 = ['a','b']
list1 = [list0, 1,2]
list2 = copy.deepcopy(list1)
list2[2] = 3
list2[0][1] = 'c'
print(list1)
print(list2)

print("hello world")