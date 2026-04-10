class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency
        # return top k frequent elements
        # I have to sort the frequency result
        # in decsending order and return the first k element
        # which data structure is most sutiable for counting and sorting at the same time?

        # the most instinct way is 
        # create a frequency hash map {num: frequency}
        # sort by the values (frequency)? 
        # then how can I get the corresponding num of the frequency?
        # use tuple? [num, frequency]
        # list[(num, frequency)], then sort by the frequency

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
    
        sorted_result = sorted(list(counter.items()), key = lambda x: x[1], reverse=True)

        return [num for num, frequency in sorted_result[:k]]