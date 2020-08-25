from math import pow
from matplotlib import pyplot


def main():
    q2()


def q2():
    def f(t, w): return w/(1+t)
    h_vals = [1, 0.5, 0.25]
    t_0, t_f, y_0 = 0, 1, 1

    print("(Midpoint method)")
    for h in h_vals:
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        print(f"h={h}")
        for _ in range(steps):
            y_prev = y
            y = y_prev + h*f(t+h/2, y_prev+h/2*f(t, y_prev))
            print(f"  t={t}, y={y}")
            t += h


if __name__ == "__main__":
    main()
