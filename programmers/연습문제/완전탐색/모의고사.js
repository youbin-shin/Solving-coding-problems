function solution(answers) {
    let answer = []
    let score_list = [] // 수포자 3명의 점수를 기록할 리스트
    let max_score = 0
    let testers = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    // 수포자 점수 측정
    for (let t = 0; t < 3; t ++) {
        let score = 0
        for (let a = 0; a < answers.length; a ++) {
            if (answers[a] === testers[t][a % testers[t].length]) {
                score += 1
            }
        }
        if (max_score < score) {
            max_score = score
        }
        score_list.push(score)     
    }
    // 가장 높은 점수 받은 사람 오름차순으로 저장
    for (let t2 = 0; t2 < 3; t2 ++) {
        if (max_score == score_list[t2]) {
            answer.push(t2 + 1)
        }
    }
    return answer;
}

// let answers = [1, 2, 3, 4, 5]
// console.log(solution(answers))