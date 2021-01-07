function solution(numbers) {
    let answer = [];
    let temp = 0
    // 두개 뽑기 위한 반복문
    for (let i = 0; i < numbers.length - 1; i ++) {
        for (let j = i + 1; j < numbers.length; j ++) {
            temp = numbers[i] + numbers[j]
            if (answer.includes(temp) === false) { // 더한 값이 answer에 없으면 추가
                answer.push(temp)
            }
        }
    }
    // 오름차순 정렬
    answer.sort(function(a, b) {
        return a - b
    })
    return answer;
}

// console.log(solution([2, 1, 3, 4, 1]))