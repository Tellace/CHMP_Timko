import numpy as np

def task1_1_3():
    A=np.matrix([
        [1,1,1,],
        [0,1,1,],
        [0,0,1,],
    ])
    B=np.matrix([
        [7,5,3,],
        [0,7,5,],
        [0,0,7,],
    ])
    rezult=A*B-B*A
    print(f"\ntask 1\n{rezult}")

def task1_2_2():
    A=np.array([
        [-1, 0, 2],
        [0, 1, 0],
        [1, 2, -1],
    ])
    rezult=A**2
    print(f"\ntask 2\n{rezult}")

def task1_3_3():
    A=np.array([
        [3, 0, 7],
        [-4, 2, 3], 
        [-1, 1, 2],
    ])
    B=np.array([
        [1],
        [2],
        [4],
    ])
    rezult=A*B
    print(f"\ntask 3\n{rezult}")

def task1_4_1():
    A=np.matrix([
        [2,3,4,],
        [1,0,6,],
        [7,8,9,],
    ])
    rezult=np.linalg.det(A)
    print(f"\ntask 4\n{rezult}")

def task1_5_2():
    A=np.array([
        [2, 3, 4, 1],
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [4, 1, 2, 3],
    ])
    rezult=np.linalg.det(A)
    print(f"\ntask 5\n{rezult}")

def task1_6_1():
    A=np.array([
        [1, 2, -3],
        [0, 1, 2],
        [0, 0, 1],
    ])
    rezult=np.linalg.inv(A)
    print(f"\ntask 6\n{rezult}")

def task1_7_1():
    A=np.array([
        [1, 2, 3, 4],
        [3, -1, 2, 5],
        [1, 2, 3, 4],
        [1, 3, 4, 5],
    ])
    rezult=np.linalg.matrix_rank(A)
    print(f"\ntask 7\n{rezult}")
    

def task1_8_1():
    a=np.array([[14,4,6],[5, -3, 2],[10, -11, 5]])
    b=np.array([[30],[15],[36]])
    array_det = np.linalg.det(a)
    X_m = np.matrix(a)
    X_m[:, 0] = b
    Y_m = np.matrix(a)
    Y_m[:, 1] = b
    Z_m = np.matrix(a)
    Z_m[:, 2] = b
    x = np.linalg.det(X_m) / array_det
    y = np.linalg.det(Y_m) / array_det
    z = np.linalg.det(Z_m) / array_det
    c = np.linalg.solve(a, b)
    print(f"\ntask 8\n{c}")

if __name__ == "__main__":
    task1_1_3()
    task1_2_2()
    task1_3_3()
    task1_4_1()
    task1_5_2()
    task1_6_1()
    task1_7_1()
    task1_8_1()
