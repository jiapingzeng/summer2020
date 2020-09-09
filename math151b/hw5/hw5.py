import math


def main():
    lin_shoot()


def lin_shoot():
    a, b = 0, math.pi/2  # endpoints
    alpha, beta = -0.3, -0.1  # boundary conditions
    Ns = [2, 4]  # intervals

    for N in Ns:
        h = (b-a)/N
        for i in range(N):
            print(i)


if __name__ == "__main__":
    main()
