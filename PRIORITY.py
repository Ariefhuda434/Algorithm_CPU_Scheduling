processes = [
    ["P1", 0, 8, 3], ["P2", 1, 4, 1], ["P3", 2, 9, 4], ["P4", 3, 5, 2],
    ["P5", 4, 2, 1], ["P6", 6, 6, 5], ["P7", 7, 3, 2], ["P8", 8, 7, 3]
]

time = 0
done = []
total_wt = total_tat = total_rt = 0
gantt_chart_str = ""

print("=== GANTT CHART (PRIORITY) ===")

while len(done) < len(processes):
    # Cari proses yang sudah tiba (AT <= time) dan belum selesai
    ready = [p for p in processes if p[1] <= time and p not in done]
    
    if not ready:
        time += 1
        continue

    # Pilih Priority terkecil (Logika Priority Scheduling)
    current = min(ready, key=lambda x: x[3])
    
    pid, at, bt, pri = current
    start = time
    time += bt
    ct = time
    tat = ct - at
    wt = tat - bt
    rt = start - at

    total_wt += wt
    total_tat += tat
    total_rt += rt

    gantt_chart_str += f"| {pid} ({start}-{ct}) "
    print(f"Proses {pid} (Pri {pri}) -> CT: {ct} | TAT: {tat} | WT: {wt} | RT: {rt}")
    done.append(current)

print("\nVisualisasi Gantt Chart:")
print(gantt_chart_str + "|")

n = len(processes)
print("\n===== AVERAGE =====")
print(f"Average Waiting Time     : {round(total_wt / n, 3)}")
print(f"Average Turn Around Time : {round(total_tat / n, 3)}")
print(f"Average Response Time    : {round(total_rt / n, 3)}")