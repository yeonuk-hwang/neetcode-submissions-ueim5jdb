type count struct {
	value int
	frequency int
}

type countHeap []count

func (h countHeap) Len() int {return len(h)}
func (h countHeap) Less(i, j int) bool {return h[i].frequency > h[j].frequency}
func (h countHeap) Swap(i, j int) {h[i], h[j] = h[j], h[i]}

func (h *countHeap) Push(x interface{}) {
	*h = append(*h, x.(count))
}

func (h *countHeap) Pop() interface{} {
	old := *h
	n := len(old)
	last := old[n-1]
	*h = old[:n-1]
	return last
}

func topKFrequent(nums []int, k int) []int {
	freqMap := make(map[int]int, len(nums))
	for _, num := range nums {
		freqMap[num]++
	}

	ch := make(countHeap, 0, len(freqMap))
	for k, v := range freqMap {
		count := count{value: k, frequency: v}
		ch = append(ch, count)
	}

	heap.Init(&ch)

	result := make([]int, 0, k)
	for range k {
		result = append(result, heap.Pop(&ch).(count).value)
	}
	return result
}