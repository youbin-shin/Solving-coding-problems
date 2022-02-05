class Solution {
    fun solution(s: String): String {
        var idx =  s.length / 2
        var diff = 1
        if (s.length % 2 == 0) {
            idx -= 1
            diff = 2
        }
        return s.substring(idx until idx + diff)
    }
}