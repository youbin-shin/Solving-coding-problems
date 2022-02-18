class Solution {
    fun solution(a: Int, b: Int): String {
        val monthDays = listOf(0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        var diff = b
        (1..a - 1).map { diff += monthDays[it] }
        val days = listOf("THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED")
        return days[diff % 7]
    }
}