def apply_to_list(some_list,f):
    return [f(x) for x in some_list]


strs = [1,2,3,4,5]
print(apply_to_list(strs,lambda a:a**2))



strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
sort=[len(set(x)) for x in strings]
print(sort)
strings.sort(key=lambda x:len(x)*2)
print(strings)

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(x)))

print(strings)
