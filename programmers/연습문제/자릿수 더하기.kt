// solution 1
class Solution {
    fun solution(n: Int): Int {
        return n.toString().toCharArray().map { it -> it.toInt() - 48 }.sum()
    }
}

// solution 2 시간 및 메모리 효율이 높음
class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        var n = n
        while (n != 0) {
            answer += n % 10
            n = n / 10
        }
        return answer
    }
}