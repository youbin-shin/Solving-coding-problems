function solution(board, moves) {
    let answer = 0;
    let result = [] // 바구니의 역할
    for (let i = 0; i < moves.length; i ++) {
        for (let j = 0; j < board.length; j ++) {
            if (board[j][moves[i] - 1] !== 0) { // 인형을 집어 올리는 경우
                // 이때 바구니 위의 인형과 같은 경우 (인형이 사라지는 경우)
                if (result[result.length - 1] === board[j][moves[i] - 1]) { 
                    result.pop()
                    answer += 2
                }
                // 바구니 맨 위의 인형과 다른 경우
                else {
                    result.push(board[j][moves[i] - 1])
                }
                
                board[j][moves[i] - 1] = 0
                break
            }
        }
    }
    return answer;
}

// console.log(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))