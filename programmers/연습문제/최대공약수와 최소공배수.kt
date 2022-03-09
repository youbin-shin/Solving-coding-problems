class Solution {
    fun solution(n: Int, m: Int): IntArray {
        var answer = intArrayOf()
        val max_num = if (n > m) n else m

        for (gcd in max_num downTo 1) {
            if (n % gcd == 0 && m % gcd == 0) {
                answer = intArrayOf(gcd, (n / gcd) * (m / gcd) * gcd)
                break
            }
        }
        return answer
    }
}