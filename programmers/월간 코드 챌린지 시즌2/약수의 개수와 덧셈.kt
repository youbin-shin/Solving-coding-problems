// Solution 1
class Solution {
    fun solution(left: Int, right: Int): Int {
        var answer: Int = 0
        for (i in left..right) {
            var cnt = (1..i).toList().toIntArray().filter {
                i % it == 0
            }.count()
            if (cnt % 2 == 0) { // 짝수인 경우
                answer += i
            } else {
                answer -= i
            }
        }
        return answer
    }
}

// Solution 2 (refactoring)
class Solution {
    fun solution(left: Int, right: Int): Int {
        return (left..right).map {
            i -> if ((1..i).filter {i % it == 0}.size % 2 == 0) i else -i
        }.sum()
    }
}