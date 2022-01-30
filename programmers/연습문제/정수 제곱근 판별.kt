import kotlin.math.*

class Solution {
    fun solution(n: Long): Long {
        var answer: Long = -1
        var sqrt_n = Math.sqrt(n.toDouble()).toInt()
        if (sqrt_n * sqrt_n == n.toInt()) {answer = (sqrt_n + 1).toDouble().pow(2).toLong()}
        return answer
    }
}