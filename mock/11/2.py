class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:

    def __init__(self):
        self.emp = {}

    def calc(self, employee) -> int:
        total = employee.importance

        for s in employee.subordinates:
            total += self.calc(self.emp[s])

        return total

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        target = None

        for e in employees:
            if e.id == id:
                target = e
            self.emp[e.id] = e

        return self.calc(target)

