def mat_design_code(N, M):
    mat = ""
    rev_mat = ""
    for i in range(N):
        if i == N // 2:
            for gen_mat in mat.rstrip("\n").split("\n")[::-1]:
                rev_mat += gen_mat + "\n"
            l = (M-len("WELCOME")) // 2
            mat += "-" * l + "WELCOME" + "-" * l + "\n"
            mat += rev_mat
            break
        mid_string = ".|." * ((i*2)+1)
        left_string = "-" * ((M - len(mid_string)) // 2)
        right_string = "-" * (M - len(mid_string) - len(left_string))
        mat += left_string + mid_string + right_string + "\n"
    return mat


if __name__ == "__main__":
    # N, M = list(map(int, (input().rstrip().split())))
    print(mat_design_code(9, 27))
