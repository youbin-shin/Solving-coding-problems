class Solution {
    fun solution(n: Long): Long {
        return n.toString().map { it.toInt() - 48 }.sorted().reversed().joinToString("").toLong()
    }
}