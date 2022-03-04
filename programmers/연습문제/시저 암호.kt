class Solution {
    fun solution(s: String, n: Int): String {
        return s.map {
            when {
                it.isLowerCase() -> {
                    var next_s = it.toInt() + n
                    if (next_s > 122) {(next_s - 26).toChar()}
                    else {next_s.toChar()}
                }
                it.isUpperCase() -> {
                    var next_s = it.toInt() + n
                    if (next_s > 90) {(next_s - 26).toChar()}
                    else {next_s.toChar()}
                }
                else -> " "
            }
        }.joinToString("")
    }
 }