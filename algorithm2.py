def calculatetask(etc, tn, pn):
    tasklist = []
    min_val = 0
    for i in range(len(etc[0])):
        if etc[0][i] == -1:
            tasklist.append(-1)
        else:
            if etc[0][i] > etc[1][i]:
                tasklist.append(1)
            else:
                tasklist.append(0)

    return tasklist

def calculateminpro(etc, taskl):
    min_val = 0
    process = 100
    task = 100
    for i in range(len(taskl)):
        if taskl[i] == -1:
            continue
        if etc[taskl[i]][i] > min_val:
            min_val = etc[taskl[i]][i]
            process = taskl[i]
            task = i

    return process, task

etc = [[140, 20, 60],
       [100, 100, 70]]

p = [0, 0]

for x in range(3):
    tasklist = calculatetask(etc, len(etc[0]), 2)
    process, task = calculateminpro(etc, tasklist)
    p[process] += etc[process][task]
    etc[0][task] = -1
    etc[1][task] = -1
    for i in range(len(etc[0])):
        if etc[process][i] != -1:
            etc[process][i] += p[process]
    print(f"processer 1 = {p[0]} and processor 2 = {p[1]}")

