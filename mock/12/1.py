class Solution:
    def __init__(self):
        self.summary = {}

    def count_domain(self, count, domain):
        if domain in self.summary:
            self.summary[domain] += count
        else:
            self.summary[domain] = count

        sub = domain.split('.')
        if len(sub) > 1:
            return self.count_domain(count, ".".join(sub[1:]))

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        for d in cpdomains:
            count, domain = d.split()
            self.count_domain(int(count), domain)

        ans = []
        for key in self.summary.keys():
            ans.append("%d %s" %(self.summary[key], key))

        return ans