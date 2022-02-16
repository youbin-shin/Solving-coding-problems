class Solution {
    fun solution(x: Int): Boolean {
        val x_sum = x.toString().map { it -> it.toInt() - 48 }.sum()
        return x % x_sum == 0
    }
}