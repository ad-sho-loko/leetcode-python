class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {}

        for i, l in enumerate(list1):
            m1[l] = i

        r = {}
        for i, l in enumerate(list2):
            if l in m1.keys():
                r[l] = m1[l] + i

        ans = []
        mini = 100001
        for key in r.keys():
            if r[key] == mini:
                ans.append(key)

            elif r[key] < mini:
                ans = [key]
                mini = r[key]

        return ans
