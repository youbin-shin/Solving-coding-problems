class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = Array(arr1.size, {IntArray(arr1[0].size, {0})})
        (arr1.indices).map { i ->
            arr1[0].indices.map { j ->
                answer[i][j] = arr1[i][j] + arr2[i][j]
            }
        }
        return answer
    }
}