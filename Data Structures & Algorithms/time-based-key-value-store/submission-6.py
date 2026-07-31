class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list) # key: (timestamp, value)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # stores they key with the value at given timestamp
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # returns a value such that Set was called previously, with timestamp_prev <= timestamp
        # return the value associtaed with the largest timestamp_prev
        if not key in self.hashmap: return ""

        arr = self.hashmap[key]
        L, R = 0, len(arr) - 1
        res = ""
        while L <= R:
            mid = (L + R) // 2
            if arr[mid][0] <= timestamp:
                L = mid + 1
                res = arr[mid][1]
            else:
                R = mid - 1

        return res
            

        