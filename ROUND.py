from collections import deque

processes = [
    ["P1", 0, 8], ["P2", 1, 4], ["P3", 2, 9], ["P4", 3, 5],
    ["P5", 4, 2], ["P6", 6, 6], ["P7", 7, 3], ["P8", 8, 7]
]

quantum = 3
remaining = {p[0]: p[2] for p in processes}
response = {}
time = 0
finished = 0
queue = deque()
total_wt = total_tat = total_rt = 0
gantt_chart_str = ""

in_queue = {p[0]: False for p in processes}

print("=== PROSES EKSEKUSI (ROUND ROBIN) ===")

while finished < len(processes):
    for p in processes:
        if p[1] <= time and not in_queue[p[0]] and remaining[p[0]] > 0:
            queue.append(p)
            in_queue[p[0]] = True

    if not queue:
        time += 1
        continue

    current = queue.popleft()
    pid, at, bt = current[0], current[1], current[2]

    if pid not in response:
        response[pid] = time - at

    run = min(quantum, remaining[pid])
    start = time
    time += run
    remaining[pid] -= run
    gantt_chart_str += f"| {pid} ({start}-{time}) "

    for p in processes:
        if p[1] <= time and not in_queue[p[0]] and remaining[p[0]] > 0:
            queue.append(p)
            in_queue[p[0]] = True

    if remaining[pid] > 0:
        queue.append(current)
    else:
        ct = time
        tat = ct - at
        wt = tat - bt
        rt = response[pid]
        total_wt += wt
        total_tat += tat
        total_rt += rt
        print(f"Proses {pid} -> CT: {ct} | TAT: {tat} | WT: {wt} | RT: {rt}")
        finished += 1

print("\nVisualisasi Gantt Chart:")
print(gantt_chart_str + "|")

n = len(processes)
print("\n===== AVERAGE =====")
print(f"Average Waiting Time     : {round(total_wt / n, 3)}")
print(f"Average Turn Around Time : {round(total_tat / n, 3)}")
print(f"Average Response Time    : {round(total_rt / n, 3)}")
