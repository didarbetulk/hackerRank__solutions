def morganAndString(a, b):
    i = 0
    j = 0
    la = len(a)
    lb = len(b)
    result = []

    while i < la and j < lb:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            ia = i
            jb = j
            while ia < la and jb < lb and a[ia] == b[jb]:
                ia += 1
                jb += 1
            if ia == la:
                result.append(b[j])
                j += 1
            elif jb == lb:
                result.append(a[i])
                i += 1
            elif a[ia] < b[jb]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

    if i < la:
        result.extend(a[i:])
    if j < lb:
        result.extend(b[j:])
    return ''.join(result)

# main code for reading input and printing output
t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    print(morganAndString(a, b))
  #henüz 17 testten yalnızca 5 tanesini geçebildi... 
