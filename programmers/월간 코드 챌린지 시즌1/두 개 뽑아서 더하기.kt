class Solution {
    fun solution(numbers: IntArray): List<Int> {
        var answer: IntArray = intArrayOf()
        for ((index, num) in numbers.withIndex()) {
            for ((index2, num2) in numbers.withIndex()) {
                if (index != index2) {
                    answer += num + num2
                }
            }
        }
        return answer.distinct().sorted()
    }
}