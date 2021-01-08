function solution(participant, completion) {
    participant.sort()
    completion.sort()
    let answer = participant[participant.length - 1]
    for (let i = 0; i < completion.length; i ++) {
        if (completion[i] !== participant[i]) {
            answer = participant[i]
            break
        }        
    }
    return answer;
}


// let participant = ["leo", "kiki", "eden"]
// let completion = ["eden", "kiki"]
// console.log(solution(participant, completion))