class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values)
        while l < r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                l = m + 1
            else:
                r = m
        return values[l - 1][0] if l > 0 else ""