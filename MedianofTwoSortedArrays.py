class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        med_ele = len(nums1)/2
        n = len(nums1)
        if (n%2==0):
            median = (nums1[int(med_ele)]+nums1[int(med_ele)-1])/2
        else:
            median = nums1[int(len(nums1)/2)]
        return median
