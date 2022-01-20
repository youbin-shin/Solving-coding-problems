# javascript 유용한 개념 정리

## array

```javascript
let arr = [1, 2, 3, 4, 5]

console.log(arr.length) // 5
arr.pop() // arr = [1, 2, 3, 4]
arr.push(8) // arr = [1, 2, 3, 4, 8]

arr.includes(3) // true
arr.includes(0) //false
```

- 길이 : length
- 추가 삭제 : push, pop
- 요소 있는지 체크 : includes

- 정렬 : sort()

  ```javascript
  // 숫자 오름차순 정렬
  
  arr.sort(function(a, b) {
          return a - b
  })
  ```

- 슬라이싱 : slice

  ```javascript
  const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];
  
  console.log(animals.slice(2));
  // expected output: Array ["camel", "duck", "elephant"]
  
  console.log(animals.slice(2, 4));
  // expected output: Array ["camel", "duck"]
  
  console.log(animals.slice(1, 5));
  // expected output: Array ["bison", "camel", "duck", "elephant"]
  ```

- 거꾸로 정렬하기 : reverse

  ```javascript
  arr.reverse()
  ```

- array 합치기 : concat()

  - python에서 extend~

  ```javascript
  arr1 = arr1.concat(arr2)
  // arr1에 arr2 합쳐진다!
  ```

- 합계 구하기 : `array.reduce()`

  ```javascript
  const array1 = [1, 2, 3, 4];
  const reducer = (accumulator, currentValue) => accumulator + currentValue;
  
  // 1 + 2 + 3 + 4
  console.log(array1.reduce(reducer));
  // expected output: 10
  
  // 5 + 1 + 2 + 3 + 4
  console.log(array1.reduce(reducer, 5));
  // expected output: 15
  ```

- 배열 만들 때 0으로 채워서 초기화하기 : `array.fill(0)`

  ```javascript
  let nums = [1, 3, 5, 10, 100];
  nums.fill(0);
  
  // 출력결과 아래
  [0, 0, 0, 0, 0]
  
  nums.fill();
  
  // 출력결과 아래
  [undefined, undefined, undefined, undefined, undefined]
  ```

  - 문법 추가 : **fill(변경할 값, 시작 위치, 끝 위치)**

    ```javascript
    nums.fill(0, 0, 2);
    
    // 출력결과 아래
    [0, 0, 5, 10, 100]
    ```

  ---

  ```javascript
  const n = 3;
  let nums = new Array(n + 1).join('0').split('').map(parseFloat)
  ```

  

---

### 아스키코드

- 문자열이나 숫자를 아스키코드로 변환하기 : `값.charCodeAt(0)`

  ```javascript
  "A".charCodeAt(0) // 65
  ```

## new Date(year, month[, day, hour, minute, second, millisecond])

| 인수        | 내용                                                         |
| :---------- | :----------------------------------------------------------- |
| year        | 1900년 이후의 년                                             |
| month       | 월을 나타내는 **0 ~ 11**까지의 정수 (주의: 0부터 시작, 0 = 1월) |
| day         | 일을 나타내는 1 ~ 31까지의 정수                              |
| hour        | 시를 나타내는 0 ~ 23까지의 정수                              |
| minute      | 분을 나타내는 0 ~ 59까지의 정수                              |
| second      | 초를 나타내는 0 ~ 59까지의 정수                              |
| millisecond | 밀리초를 나타내는 0 ~ 999까지의 정수                         |

```javascript
// 월을 나타내는 4는 5월을 의미한다.
// 2019/5/1/00:00:00:00
let date = new Date(2019, 4);
console.log(date); // Wed May 01 2019 00:00:00 GMT+0900 (한국 표준시)

// 월을 나타내는 4는 5월을 의미한다.
// 2019/5/16/17:24:30:00
date = new Date(2019, 4, 16, 17, 24, 30, 0);
console.log(date); // Thu May 16 2019 17:24:30 GMT+0900 (한국 표준시)

// 가독성이 훨씬 좋다.
date = new Date('2019/5/16/17:24:30:10');
console.log(date); // Thu May 16 2019 17:24:30 GMT+0900 (한국 표준시)
```

- 요일 정수로 반환

  ```javascript
  const today = new Date();
  const day = today.getDay();
  
  console.log(today); // Thu May 16 2019 17:47:31 GMT+0900 (한국 표준시)
  console.log(day);   // 4
  ```

  |  요일  | 반환값 |
  | :----: | :----: |
  | 일요일 |   0    |
  | 월요일 |   1    |
  | 화요일 |   2    |
  | 수요일 |   3    |
  | 목요일 |   4    |
  | 금요일 |   5    |
  | 토요일 |   6    |



### int 형

```javascript
let n = 10
n = parseInt(n / 3) // n = 3
```

### 진수 변환

```javascript
parseInt(n, 3) // n을 3진수로 바꿔준다!
```

### 이용한 메소드

```javascript
let temp = n.toString(3).split('').reverse().join('')
```

- `.toString(3)` : 3진수로 변환
- `.split('')` : 간격대로 끊어서 리스트로 바꿔준다!
- `.reverse()` : 역으로 순서를 바꿔준다.
- `.join('')` : 리스트요소들을 문자열로 합쳐준다.





## 재귀함수

```javascript
function factorial(fnum){
  end_num = 1;
  if(fnum == end_num) return end_num;
  else return fnum*factorial(fnum-1);
}
document.write(factorial(3));
```

