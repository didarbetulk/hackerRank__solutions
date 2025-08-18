# Palindrome Index - O(n) sorusu
# Bir string icinde en fazla 1 karakter silerek palindrome yapialbilr mi?
# if evet -> silinecek karakterin indexi
# if hayır veya zaten palindrome ise -> -1

import sys 

def palindrome_index(s: str) -> int:
    i, j = 0, len(s) - 1  # i=sol uc, j=sag uctab basla
    
  # iki taraftan karsilastir,eslesenleri atla
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
      
    # already a palindrome
    if i >= j:
        return -1

    # yardimci fonk: check if s[l:r+1] is a palindrome
    def is_pal(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # try removing left mismatch or right mismatch/ sol sag hicbiri 
    if is_pal(i + 1, j):
        return i
    if is_pal(i, j - 1):
        return j
    return -1

def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return
    q = int(lines[0])
    out = []
    for t in range(1, q + 1):
        out.append(str(palindrome_index(lines[t].strip())))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
