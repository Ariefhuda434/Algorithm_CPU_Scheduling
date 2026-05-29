processes = [
    ["P1", 0, 8], ["P2", 1, 4], ["P3", 2, 9], ["P4", 3, 5],
    ["P5", 4, 2], ["P6", 6, 6], ["P7", 7, 3], ["P8", 8, 7]
]

n = len(processes)
remaining = {p[0]: p[2] for p in processes}
response = {}
finish_data = [] 

time = 0
finished = 0
last_pid = None
gantt_chart_str = ""

print("=== PROSES EKSEKUSI (SRTF) ===")

while finished < n:
    ready = [p for p in processes if p[1] <= time and remaining[p[0]] > 0]

    if len(ready) == 0:
        time += 1
        continue

    current = min(ready, key=lambda x: remaining[x[0]])
    pid = current[0]
    at = current[1]
    bt = current[2]

    if pid not in response:
        response[pid] = time - at

    if pid != last_pid:
        gantt_chart_str += f"| {pid} ({time}-"
    
    remaining[pid] -= 1
    time += 1
    
    if pid != last_pid:
        pass
    
    next_ready = [p for p in processes if p[1] <= time and remaining[p[0]] > 0]
    next_pid = None
    if next_ready:
        next_pid = min(next_ready, key=lambda x: remaining[x[0]])[0]

    if next_pid != pid or remaining[pid] == 0:
        gantt_chart_str += f"{time}) "

    if remaining[pid] == 0:
        ct = time
        tat = ct - at
        wt = tat - bt
        rt = response[pid]
        
        finish_data.append([pid, at, bt, ct, tat, wt, rt])
        print(f"Proses {pid} -> CT: {ct} | TAT: {tat} | WT: {wt} | RT: {rt}")
        finished += 1

    last_pid = pid

print("\nVisualisasi Gantt Chart:")
print(gantt_chart_str + "|")

total_wt = sum(d[5] for d in finish_data)
total_tat = sum(d[4] for d in finish_data)
total_rt = sum(d[6] for d in finish_data)

print("\n===== AVERAGE =====")
print(f"Average Waiting Time     : {round(total_wt / n, 3)}")
print(f"Average Turn Around Time : {round(total_tat / n, 3)}")
print(f"Average Response Time    : {round(total_rt / n, 3)}")