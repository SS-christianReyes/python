print(list[1,'hello',2.4])
l = [1,[1,2]]
print(l[1][1])
lst=['a','b','c'] 
print(lst[1:])
week = {
    'Monday' : 1,
    'Tuesday' : 2,
    'Wednesday' : 3,
    'Thursday' : 4,
    'Friday' : 5,
    'Saturday' : 6,
    'Sunday' : 7
}
print(week)
d={'k1':[1,2,3]}
print(d['k1'][1])
print(tuple([1,[2,3]]))
word = set('Mississipi')
word.add('X')
print(word)
print(set([1,1,2,3]))

#divisible by 7 but not a multiple of 5
r = range(2000,3200)
def divisibleBy7(r):
    numbers = set()
    for i in r:
        if i % 7 == 0 and i % 5 != 0:
            numbers.add(i)
    return numbers
print(divisibleBy7(r))
