class Solution {
    fun solution(numbers: IntArray): Int {
        val numberList = (0..9).toList().toIntArray()
        return numberList.filter {
            !numbers.contains(it)
        }.sum()
    }
}