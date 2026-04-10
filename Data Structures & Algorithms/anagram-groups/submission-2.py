class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # one hashmap per each anagram set
        # calculate hashmap for each str
        # add them to the hashmap list [{}, {}, {}]
        # if same hash map is in the hashmap list, add them to the corresponding sublist of the result
        # if not, add them to the new sublist

        counters = list()
        result = list()

        for str in strs:
            counter = {}

            for c in str:
                counter[c] = counter.get(c, 0) + 1
            
            if counter in counters:
                index = counters.index(counter)
                result[index].append(str)
            else:
                counters.append(counter)
                result.append([str])
                
        return result