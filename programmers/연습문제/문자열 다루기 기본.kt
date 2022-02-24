class Solution {
    fun solution(s: String): Boolean {
        return (s.toIntOrNull() != null && (s.length == 4 || s.length == 6))
    }
}