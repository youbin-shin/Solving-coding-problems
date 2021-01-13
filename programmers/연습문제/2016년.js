function solution(a, b) {
    let day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    let date2 = new Date(`2016,${a},${b}`);
    return day[date2.getDay() % 7];
}


// let a = 5
// let b = 24
// console.log(solution(a, b))