class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer: Int = 0
        absolutes.forEachIndexed{
            index, value -> answer += (if (signs[index]) 1 else -1) * value
        }
        return answer
    }
}