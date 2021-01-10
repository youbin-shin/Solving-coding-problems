function solution(n, lost, reserve) {
    let answer = n - lost.length;

    // 여벌의 체육복을 가져온 학생이 도난당한 경우 찾기
    for (let i = 0; i < reserve.length; i ++) {
        if (lost.includes(reserve[i])) {
            lost[lost.indexOf(reserve[i])] = -1

            reserve[i] = -1
            answer += 1
        }
    }
    // 여벌 체육복을 도난당한 학생들에게 빌려주는 경우 찾기 
    for (let r = 0; r < reserve.length; r ++) {
        if (reserve[r] === -1) { 
            continue
        }
        for (let l = 0; l < lost.length; l ++) {
            if (lost[l] === -1) {
                continue
            }
            else if (lost[l] === reserve[r] - 1 || lost[l] === reserve[r] + 1) {
                    answer += 1
                    lost[l] = -1
                    break

            }
        }
    }
    return answer;
}


// let n = 7
// let lost = [2, 3, 4]
// let reserve = [1, 2, 3, 6]
// console.log(solution(n, lost, reserve))