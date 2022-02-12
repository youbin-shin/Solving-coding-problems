class Solution {
    fun solution(phone_number: String): String {
        val len = phone_number.length
        return (1..len - 4).map{"*"}.joinToString(separator ="") + phone_number.substring(len - 4 until len)
    }
}