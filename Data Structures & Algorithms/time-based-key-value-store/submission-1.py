class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp,value])
        
    def search_util(self, values:List(), target: int) -> str :
        low,high = 0, len(values)-1
        result = ""

        while(low<=high):
            mid = (high+low)//2
            if (values[mid][0]<=target):
                result = values[mid][1]
                low = mid+1
            else:
                high = mid-1

        return result

    def get(self, key: str, timestamp: int) -> str:
        val_ts = self.time_map.get(key,[])
        return self.search_util(val_ts,timestamp)

        
