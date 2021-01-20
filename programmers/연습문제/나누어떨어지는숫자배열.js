function solution(arr, divisor) {
    let answer = [];
    // 나누어 떨어지는 값 찾기
    for (let i = 0; i < arr.length; i ++) {
        if (arr[i] % divisor === 0) {
            answer.push(arr[i])
        }
    }
    // 오른차순으로 정렬하기
    answer.sort(function(a, b) {
        return a - b
    })
    // 빈배열일 조건 만족하기
    if (answer.length === 0) {
        answer = [-1]
    }
    return answer;
}