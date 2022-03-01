class Solution {
    fun solution(s: String): String {
        var isEven = 1
        var answer = ""
        (s.indices).map {
            i ->
            if (!s[i].isLetter()) {
                answer += s[i]
                isEven = 1
            } else {
                answer += if (isEven == 1) s[i].toUpperCase() else s[i].toLowerCase()
                isEven = if (isEven== 1) 0 else 1
            }
        }
        return answer
    }
}