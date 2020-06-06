s = set()
s


t = (1,2,3,"ali")
s = set(t)
s

ali = "lutfen buraya gelin"
type(ali)
s = set(ali)
s
len(s)
s[0]


l = ["gelecegi","yazanlar"]
s = set(l)
s
dir(s)
s.add("ile")
s

s.add("ile")
s
s.remove("ile")
s

s.remove("ile")


s.discard("ile")
s


# =============================================================================
# difference
# =============================================================================

set1 = set([1,3,5])
set2 = set([1,4,5])

set1.difference(set2)
set1.symmetric_difference(set2)

dir(set1)

set1.intersection(set2)

set1 & set2

kesisim = set1.intersection(set2)
set1.union(set2)

set1.intersection_update(set2)
set1

#set sorgu islemleri

set1 = set([7,8,9,])

set2 = set([5,6,7,8,9,10])

set1.isdisjoint(set2)


set1.issubset(set2)
set2.issuperset(set1)



