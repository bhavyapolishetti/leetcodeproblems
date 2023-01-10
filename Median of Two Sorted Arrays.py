# leetcodeproblems
this repo includes solutions  of Leet code problems in python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=[]
        i=0
        j=0
        a=len(nums1)
        b=len(nums2)
        while i<a and j<b:
            if nums1[i]<=nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1 
        while i<a:
            l.append(nums1[i])
            i+=1 
        while j<b:
            l.append(nums2[j])
            j+=1 
        if len(l)%2==0:
            c=l[len(l)//2-1]+l[(len(l)//2)]
            return c/2
        else:
            return l[len(l)//2]
