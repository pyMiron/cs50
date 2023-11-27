def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number= el
    return min_number



nums1=[4,567,7,8,9,1,3,2,1]
min1=minimal(nums1)

nums2=[3.5,6.7,7.8,9.0]
min2=minimal(nums2)
if min1 < min2:
    print(min1)
else:
    print(min2)