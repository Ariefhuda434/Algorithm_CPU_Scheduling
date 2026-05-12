processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 1],
    ["P4", 3, 4]
]

time = 0
done = []

# Variabel total
total_wt = 0
total_tat = 0
total_rt = 0

print("Gantt Chart:")

while len(done) < len(processes):

    ready = []

    for p in processes:
        if p[1] <= time and p not in done:
            ready.append(p)

    if len(ready) == 0:
        time += 1
        continue

    # Memilih burst time terkecil
    current = min(ready, key=lambda x: x[2])

    pid = current[0]
    at = current[1]
    bt = current[2]

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

    done.append(current)

# Menghitung average
n = len(processes)

avg_wt = total_wt / n
avg_tat = total_tat / n
avg_rt = total_rt / n

print("===== AVERAGE =====")
print("Average Waiting Time     :", round(avg_wt, 2))
print("Average Turn Around Time :", round(avg_tat, 2))
print("Average Response Time    :", round(avg_rt, 2))