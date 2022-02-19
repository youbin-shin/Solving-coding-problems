class Solution {
    fun solution(answers: IntArray): IntArray {
        var answer = ArrayList<Int>()
        val students = arrayOf(
            intArrayOf(1, 2, 3, 4, 5),
            intArrayOf(2, 1, 2, 3, 2, 4, 2, 5),
            intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        )
        var scores = intArrayOf(0, 0, 0)
        (answers.indices).map { a ->
            (0..2).map { s ->
                var index = a % students[s].size
                if (answers[a] == students[s][index]) {
                    scores[s] += 1
                }
            }
        }
        (scores.indices).map {
            if (scores[it] == scores.max()) {
                answer.add(it + 1)
            }
        }
        return answer.toIntArray()
    }
}
