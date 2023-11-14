class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        mostTime = logs[0][1]
        longestWorkingEmployee = logs[0][0]
        lastTaskEnded = mostTime
        for log in logs[1:]:
            if (log[1] - lastTaskEnded) > mostTime:
                longestWorkingEmployee = log[0]
                mostTime = (log[1] - lastTaskEnded)
            elif (log[1] - lastTaskEnded) == mostTime:
                if log[0] < longestWorkingEmployee:
                    longestWorkingEmployee = log[0]
            lastTaskEnded = log[1]
        return longestWorkingEmployee
