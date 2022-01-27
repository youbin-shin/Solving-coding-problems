class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        var finalRow: Int = 0
        var finalCol: Int = 0
        sizes.map {
            var row = it[0]
            var col = it[1]
            if (it[0] < it[1]) {
                var temp = it[1]
                col = row
                row = temp
            }
            if (finalRow < row) {finalRow = row}
            if (finalCol < col) {finalCol = col}
        }
        return finalCol * finalRow
    }
}