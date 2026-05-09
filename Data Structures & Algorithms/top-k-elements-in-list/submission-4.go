type Count struct {
	value int
	count int
}

type Heap struct {
	data []Count
	cap  int
	less func(a, b Count) bool
}

func NewHeap(k int) *Heap {
	return &Heap{
		cap: k,
		less: func(a, b Count) bool {
			return a.count < b.count
		},
	}
}

func (h *Heap) Push(c Count) {
	h.data = append(h.data, c)
	h.siftUp(len(h.data) - 1)
	if len(h.data) > h.cap {
		h.Pop()
	}
}

func (h *Heap) siftUp(i int) {
	for i > 0 {
		parent := (i - 1) / 2

		if h.less(h.data[i], h.data[parent]) {
			h.data[parent], h.data[i] = h.data[i], h.data[parent]
			i = parent
		} else {
			break
		}
	}
}

func (h *Heap) Pop() (Count, bool) {
	if len(h.data) == 0 {
		var zero Count
		return zero, false
	}

	root := h.data[0]
	last := h.data[len(h.data)-1]
	h.data[0] = last
	h.data = h.data[:len(h.data)-1]

	h.siftDown(0)

	return root, true
}

func (h *Heap) siftDown(i int) {
	n := len(h.data)
	for {
		smallest := i
		left := i*2 + 1
		right := i*2 + 2

		if left < n && h.less(h.data[left], h.data[smallest]) {
			smallest = left
		}

		if right < n && h.less(h.data[right], h.data[smallest]) {
			smallest = right
		}

		if smallest == i {
			break
		}

		h.data[smallest], h.data[i] = h.data[i], h.data[smallest]
		i = smallest
	}
}


func topKFrequent(nums []int, k int) []int {
	counts := make(map[int]Count) 

	for _, num := range nums {
		org := counts[num]
		counts[num] = Count{
			value: num,
			count: org.count + 1,
		}
	}

	h := NewHeap(k)
	for _, c := range counts {
		h.Push(c)
	}

	var result []int

	for range k {
		val, _ := h.Pop()
		result = append(result, val.value)
	}
	return result
}
