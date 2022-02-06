// Solution 1
class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        var answer: Long = 0
        answer -= money
        (1..count).toList().toIntArray().forEach {
            answer += it * price
        }
        if (answer < 0) {
            return 0
        }
        return answer
    }
}


// Solution 2
class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        return (1..count).map { it * price.toLong() }.sum().let { if (money > it) 0 else it - money }
    }
}