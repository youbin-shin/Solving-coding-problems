class Solution {
    fun solution(arr: IntArray): IntArray {
        val minValue = arr.min()
        var answer = arr.filter { it != minValue }.toIntArray()
        if (answer.isEmpty()) {
            answer = intArrayOf(-1)
        }
        return answer
    }
}