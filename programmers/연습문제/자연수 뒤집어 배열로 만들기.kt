class Solution {
    fun solution(n: Long): IntArray {
        return n.toString().map { it.toInt() - 48 }.reversed().toIntArray()
    }
}