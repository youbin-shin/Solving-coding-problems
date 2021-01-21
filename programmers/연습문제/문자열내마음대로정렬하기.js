function solution(strings, n) {
    let answer = [];
    let str_list = []
    // str_list 에 n번의 알파벳과 인덱스 번호 저장하기
    for (let i = 0; i < strings.length; i ++) {
        str_list.push([strings[i][n], i])
    }
    str_list.sort() // n번의 알파벳 순으로 정렬하기

    let temp = [] // 인덱스가 동일한 경우 사전순으로 정렬하기 위해 임시로 저장할 리스트
    for (let j = 0; j < strings.length; j ++) {
        // 동일한 n번의 알파벳을 갖는 경우 temp에 해당 단어 저장하기
        if (j != strings.length - 1 && str_list[j][0] == str_list[j + 1][0]) {
            if (temp.includes(strings[str_list[j][1]]) === false) {
                temp.push(strings[str_list[j][1]])
            }
            if (temp.includes(strings[str_list[j + 1][1]]) === false) {
                temp.push(strings[str_list[j + 1][1]])
            } 
        } else {
            if (temp.length > 0) {
                // temp 단어 사전순으로 정렬해서 answer에 추가하기
                temp.sort()
                answer = answer.concat(temp)
                temp = []
            } else {
                // 그 외의 경우 순서대로 저장하기
                answer.push(strings[str_list[j][1]])
            }
        }
    }
    if (temp.length > 0) {
                temp.sort()
                answer.concat(temp)
    }
    return answer;
}