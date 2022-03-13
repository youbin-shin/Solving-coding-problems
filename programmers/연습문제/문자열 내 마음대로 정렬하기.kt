class Solution {
    fun solution(strings: Array<String>, n: Int): Array<Any> {
        return strings.sortedWith(compareBy({it[n]}, {it})).toTypedArray()
    }
}