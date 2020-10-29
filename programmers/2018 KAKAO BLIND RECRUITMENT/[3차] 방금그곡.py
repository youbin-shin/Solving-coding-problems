def solution(m, musicinfos):
    answer = "(None)"

    melody_list = {"C": "a", "C#": "b", "D": "c", "D#": "d", "E": "e", "F": "f", "F#": "g", "G": "h", "G#": "i", "A": "j", "A#": "k", "B": "l"}
    m_num = ""
    for i in range(len(m)): # 음을 알파벳만으로 고치기
        if m[i] == "#": continue
        temp = m[i]
        if i != len(m)-1 and m[i+1] == "#":
            temp = m[i:i+2]
        m_num += str(melody_list.get(temp))
    m = m_num

    final_time_length = 0
    for i in range(len(musicinfos)):
        # 주어진 musicinfos를 변수에 저장하기
        start_time, end_time, title, melody = musicinfos[i].split(",")
        # 재생시간 계산하기
        time_length = (int(end_time[:2])-int(start_time[:2]))*60 + (int(end_time[3::])-int(start_time[3::]))

        melody_num = ""
        for i in range(len(melody)): # 음을 알파벳만으로 고치기
            if melody[i] == "#": continue
            temp = melody[i]
            if i != len(melody) - 1 and melody[i + 1] == "#":
                temp = melody[i:i + 2]
            melody_num += str(melody_list.get(temp))
        melody = melody_num

        # 재생될 music 만들기
        if time_length >= len(melody):
            music = melody
            idx = 0
            while len(music) != time_length:
                music += melody[idx]
                idx += 1
                if idx == len(melody):
                    idx = 0
        else:
            music = melody[:time_length]

        # m과 같은 곡인지 확인하기
        for j in range(time_length-len(m)+1):
            if m == music[j:j+len(m)]:
                if time_length > final_time_length:
                    answer = title
                    final_time_length = time_length
                break
    return answer


# m = "CC#BCC#BCC#BCC#B"
# musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# print(solution(m, musicinfos))