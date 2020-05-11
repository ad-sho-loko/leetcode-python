class Log:
    def __init__(self, function_id, is_start, time):
        self.function_id = function_id
        self.is_start = is_start
        self.time = time


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not logs:
            return []

        times = [0] * n
        logging = []

        for l in logs:
            splitted = l.split(":")
            function_id = int(splitted[0])
            is_start = splitted[1] == "start"
            time = int(splitted[2])
            logging.append(Log(function_id, is_start, time))

        stack = []
        prev_consumed = 0
        for l in logging:
            if l.is_start:
                stack.append(l.time)
            else:
                pushed = stack.pop()
                consumed = l.time - pushed - prev_consumed + 1
                times[l.function_id] += consumed
                prev_consumed = consumed

        return times
