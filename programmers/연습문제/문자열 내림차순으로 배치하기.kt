class Solution {
    fun solution(s: String): String {
        return s.map { it }.sorted().reversed().joinToString("")
    }
}