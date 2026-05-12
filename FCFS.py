processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 1],
    ["P4", 3, 4]
]

time = 0

# Variabel total
total_wt = 0
total_tat = 0
total_rt = 0

print("Gantt Chart:")

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

    # Menjumlahkan total
    total_wt += wt
    total_tat += tat
    total_rt += rt

    print(f"| {pid} ({start}-{ct}) |")

    print(pid)
    print("CT :", ct)
    print("TAT:", tat)
    print("WT :", wt)
    print("RT :", rt)
    print()

# Menghitung average
n = len(processes)

avg_wt = total_wt / n
avg_tat = total_tat / n
avg_rt = total_rt / n

print("===== AVERAGE =====")
print("Average Waiting Time     :", round(avg_wt, 2))
print("Average Turn Around Time :", round(avg_tat, 2))
print("Average Response Time    :", round(avg_rt, 2))