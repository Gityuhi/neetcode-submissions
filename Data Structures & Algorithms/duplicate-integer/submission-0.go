func hasDuplicate(nums []int) bool {
    hashmap := make(map[int]int)

    for _, num := range nums {
        if _, ok := hashmap[num]; !ok {
            hashmap[num] = 1
        } else {
            return true
        }
    }
    return false
}
