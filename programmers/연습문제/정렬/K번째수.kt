import java.util.*

val inputArray = intArrayOf(1, 5, 2, 6, 3, 7, 4)
val input1 = intArrayOf(2, 5, 3)
val input2 = intArrayOf(4, 4, 1)
val input3 = intArrayOf(1, 7, 3)
val inputCommand: Array<IntArray> = arrayOf(input1, input2, input3)


// solution 1
fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
    var answer = intArrayOf()
    for (command in commands) {
        val sliceArray = array.slice(command[0] - 1..command[1] - 1)
        answer += sliceArray.sorted()[command[2] - 1]
    }

    return answer
}

// solution 2 (개선 코드)
fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
    return commands.map { command ->
        array.slice(command[0] - 1..command[1] - 1).sorted()[command[2] - 1]
    }.toIntArray()
}


fun main() {
    print(solution(inputArray, inputCommand).contentToString())
}
