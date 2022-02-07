class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        val rank: IntArray = intArrayOf(6, 6, 5, 4, 3, 2, 1)
        var zero_cnt = lottos.filter {it == 0}.size
        var win_cnt = lottos.filter { win_nums.contains(it) }.size
        return intArrayOf(rank[zero_cnt + win_cnt], rank[win_cnt])
    }
}