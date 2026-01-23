import mypkg.geotypes as gt

foo = gt.Rect((2,8), (4,12))
baz = gt.Rect((2,8), (4,12))
bar = gt.Rect((2,8), (9,12))

# print(foo)
# print(bar)
# print(foo + bar)
# print(foo - bar)
# print(foo > bar)
# print(foo < bar)
# print(foo >=baz)
# print(baz <= foo)

print(foo)
foo.lb=(1,1)
print(foo)


foo.rt=(3,9)
print(foo)

# print(foo)
# print(repr(foo))
# print(foo.__class__.__name__)
# print(foo.__class__.__qualname__)