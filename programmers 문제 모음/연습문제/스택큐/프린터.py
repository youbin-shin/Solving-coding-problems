def solution(priorities, location):
  files = []
  for p in range(len(priorities)):
    files.append([priorities[p], p])
  print_files = [] # 프린트되는 순서를 저장할 리스트
  while files:
    sort_files = sorted(files, key=lambda x: (-x[0])) # 가장 중요도가 높은 파일 순으로 정렬한 리스트
    if files[0][0] >= sort_files[0][0]: # 중요도가 가장 높은 파일이 맨 앞에 있는 경우 프린트하기
      print_files.append(files.pop(0))
      if print_files[-1][1] == location: # 추가한 파일이 찾는 파일이면 종료하기
        break
    else: # 중요도가 가장 높지 않기에 뒤로 보내기
      files.append(files.pop(0))

  return len(print_files)


# priorities = [3,3,4,2]
# location = 3
# print(solution(priorities, location)) # 정답: 4