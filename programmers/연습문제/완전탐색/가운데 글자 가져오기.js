function solution(s) {
  let half = parseInt(s.length / 2);
  if (s.length % 2) { // 글자 길이가 홀수인 경우
    return s[half];
  } else { // 글자 길이가 짝수인 경우
    return s.slice(half - 1, half + 1);
  }
}
