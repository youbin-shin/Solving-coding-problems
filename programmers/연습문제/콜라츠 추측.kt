class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        var n = n.toLong()
        while (n != 1.toLong()) {
            answer += 1
            if (answer > 500) {
                answer = -1
                break
            }
            n = if (n % 2 == 0.toLong()) n / 2 else n * 3 + 1
        }
        return answer
    }
}