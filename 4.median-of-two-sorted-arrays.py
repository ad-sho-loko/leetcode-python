class List:
    def __init__(self):
        pass

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        # ２つの配列の長さをlen(num1)<=len(num2)に限定してから以降計算したい
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n + m - 1) // 2
        l = 0
        r = min(k, n)

        # nums1を切る位置を決めていく
        # num1を切る位置によってnum2を切る位置は自動で決まる ※ len(num1) == len(num2)より
        while l < r:
            mid1 = (l + r) // 2
            mid2 = k - mid1
            if nums1[mid1] < nums2[mid2]:
                l = mid1 + 1
            else:
                r = mid1

        a = -1
        if l > 0:
            a = max(nums1[l - 1], a)
        if k - l >= 0:
            a = max(nums2[k - l], a)

        # if odd, return a.
        if (n + m) & 1:
            return a

        b = 999999999999999999999
        if l < n:
            b = min(b, nums1[l])
        if k - l + 1 < m:
            b = min(b, nums2[k - l + 1])

        # if even, return (a + b) / 2
        return (a + b) / 2