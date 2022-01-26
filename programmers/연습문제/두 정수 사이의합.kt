class Solution {
    fun solution(a: Int, b: Int): Long {
        var answer = 0L
        var a = a
        var b = b
        if (a > b) {
            a = b.also { b = a }}
        (a..b).toList().toIntArray().forEach{
            answer += it
        }
        return answer
    }
}