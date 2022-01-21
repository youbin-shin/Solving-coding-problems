def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    report_dict = {}
    for r in report:
        user_id, report_id = r.split(" ")
        if report_id not in report_dict:
            report_dict[report_id] = [user_id]
        else:
            report_dict[report_id].append(user_id)
    for key, values in report_dict.items():
        if len(values) >= k:
            for value in values:
                answer[id_list.index(value)] += 1
    return answer