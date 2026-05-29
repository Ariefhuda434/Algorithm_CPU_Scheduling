processes = [
    ["P1", 0, 8],
    ["P2", 1, 4],
    ["P3", 2, 9],
    ["P4", 3, 5],
    ["P5", 4, 2],
    ["P6", 6, 6],
    ["P7", 7, 3],
    ["P8", 8, 7]
]

time = 0
total_wt = 0
total_tat = 0
total_rt = 0

print("=== GANTT CHART ===")
gantt_chart_str = ""

for p in processes:

    pid = p[0]
    at = p[1]
    bt = p[2]

    if time < at:
        time = at

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

    print(f"Proses {pid} -> CT: {ct} | TAT: {tat} | WT: {wt} | RT: {rt}")

print("\nVisualisasi Gantt Chart:")
print(gantt_chart_str + "|")

n = len(processes)

avg_wt = total_wt / n
avg_tat = total_tat / n
avg_rt = total_rt / n

print("\n===== AVERAGE =====")
print(f"Average Waiting Time     : {round(avg_wt, 3)}")
print(f"Average Turn Around Time : {round(avg_tat, 3)}")
print(f"Average Response Time    : {round(avg_rt, 3)}")
