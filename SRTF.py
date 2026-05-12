processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 1],
    ["P4", 3, 4]
]

remaining = {}
response = {}

# Variabel total
total_wt = 0
total_tat = 0
total_rt = 0

for p in processes:
    remaining[p[0]] = p[2]

time = 0
finished = 0

print("Gantt Chart:")

while finished < len(processes):

    ready = []

    for p in processes:
        if p[1] <= time and remaining[p[0]] > 0:
            ready.append(p)

    if len(ready) == 0:
        time += 1
        continue

    # Memilih remaining time terkecil
    current = min(ready, key=lambda x: remaining[x[0]])

    pid = current[0]
    at = current[1]

    if pid not in response:
        response[pid] = time - at

    print(f"| {pid} ({time}-{time+1}) |")

    remaining[pid] -= 1
    time += 1

    if remaining[pid] == 0:

        ct = time
        bt = current[2]

        tat = ct - at
        wt = tat - bt
        rt = response[pid]

        # Menjumlahkan total
        total_wt += wt
        total_tat += tat
        total_rt += rt

        print(pid)
        print("CT :", ct)
        print("TAT:", tat)
        print("WT :", wt)
        print("RT :", rt)
        print()

        finished += 1

# Menghitung average
n = len(processes)

avg_wt = total_wt / n
avg_tat = total_tat / n
avg_rt = total_rt / n

print("===== AVERAGE =====")
print("Average Waiting Time     :", round(avg_wt, 2))
print("Average Turn Around Time :", round(avg_tat, 2))
print("Average Response Time    :", round(avg_rt, 2))