function solution(array, commands) {
    let answer = [];
    for (let c = 0; c < commands.length; c ++) {
        // 배열 array의 i번째부터 j번째 숫자까지 자르기
        let cut_array = array.slice(commands[c][0] - 1, commands[c][1])
        // 자른 배열 정렬하기
        cut_array.sort(function(a, b) {
            return a - b
        })
        // 정렬 후 k번째 있는 수 추가하기
        answer.push(cut_array[commands[c][2] - 1])
    }
    return answer;
}


// let array = [1, 5, 2, 6, 3, 7, 4] 
// let commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
// console.log(solution(array, commands))