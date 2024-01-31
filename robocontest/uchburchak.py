def uchburchak_yasash(N, tayoqchalar):
    
    tayoqchalar.sort()

    
    x, y, z = tayoqchalar[0], tayoqchalar[1], tayoqchalar[-1]

    
    if x + y > z:
        return [x, y, z]
    else:
        return -1


with open("INPUT.TXT", "r") as file:
    N = int(file.readline().strip())
    tayoqchalar = list(map(int, file.readline().split()))


with open("OUTPUT.TXT", "w") as file:
    result = uchburchak_yasash(N, tayoqchalar)
    if result == -1:
        file.write("-1")
    else:
        file.write(" ".join(map(str, result)))
