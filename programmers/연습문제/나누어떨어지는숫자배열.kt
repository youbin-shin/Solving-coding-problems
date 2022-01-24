fun solution(arr: IntArray, divisor: Int): IntArray {
    val answer =  arr.filter { it%divisor == 0 }.sorted().toIntArray()
    if (answer.isEmpty()) {
        return intArrayOf(-1)
    }
    return answer
}