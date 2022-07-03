import bisect


class TimeMap(object):

    def __init__(self):
        self.stuff = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.stuff:
            self.stuff[key][0].append(timestamp)
            self.stuff[key][1].append(value)
        else:
            self.stuff[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stuff: return ""
        times, keys = self.stuff[key]
        
        x = bisect.bisect_right(times, timestamp) - 1
        return keys[x] if x >= 0 else ""
