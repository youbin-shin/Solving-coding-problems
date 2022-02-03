class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        var answer: Int = 0
        a.forEachIndexed{
            idx, value -> answer += value * b[idx]
        }
        return answer
    }
}