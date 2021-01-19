function solution(arr)
{
    let answer = [];
    answer.push(arr.pop(0))
    
    while (arr.length > 0) {
        let temp = arr.pop()
        if (answer[answer.length - 1] !== temp) {
            answer.push(temp)
        }
    }
    return answer.reverse();
}
