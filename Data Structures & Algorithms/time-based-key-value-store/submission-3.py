class TimeMap:

    def __init__(self):
        self.timestamp_hash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_hash[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        value_pairs = self.timestamp_hash[key]

        left, right = 0, len(value_pairs) - 1

        res = ""
        while left <= right:
            middle = left + ((right - left) // 2)

            retrived_timestamp = value_pairs[middle][0]

            if retrived_timestamp == timestamp:
                return value_pairs[middle][1]
            elif retrived_timestamp < timestamp:
                res = value_pairs[middle][1]
                left = middle + 1
            elif retrived_timestamp > timestamp:
                right = middle - 1

        return res


                

        
