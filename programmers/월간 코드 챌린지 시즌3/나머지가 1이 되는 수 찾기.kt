// solution 1 (시간 효율 높음)
class Solution {
    fun solution(n: Int): Int {
        var answer: Int = n + 1
    for (i in 1..n) {
        if (n % i == 1) {
            return i
        }
    }
    return answer
    }
}


// solution 2
class Solution {
    fun solution(n: Int): Int {
        return (1.. n + 1).filter { n % it == 1 }.first()
    }
}