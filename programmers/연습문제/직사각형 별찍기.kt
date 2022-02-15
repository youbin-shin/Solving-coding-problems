fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    (1..b).map{
        println((1..a).map{"*"}.joinToString(separator =""))
    }
}