from math import pow, exp


def main():
    q3c()


def q2b():
    h_vals = [0.5, 0.2, 0.1, 0.01]  # step sizes
    t_0, t_f, y_0 = 1, 2, 2  # initial/final values

    for h in h_vals:
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        for _ in range(steps):
            y_prev = y
            y = y_prev + h*(1+t)/(1+y_prev)
            t += h
        print(f"h={h}, y={y}")


def q3c():
    h_vals = [0.5, 0.1, 0.01]  # step sizes
    t_0, t_f, y_0 = 0, 1, 1  # initial/final values

    print("(Euler's method)")
    for h in h_vals:
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        for _ in range(steps):
            y_prev = y
            y = y_prev + h*pow(y_prev, 2)*exp(-t)
            t += h
        print(f"h={h}, y={y}, error={exp(1)-y}")

    print("(Taylor method)")
    for h in h_vals:
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        for _ in range(steps):
            y_prev = y
            y = y_prev + h*pow(y_prev, 2)*exp(-t) + pow(h, 2) * \
                (-1*pow(y_prev, 2)*exp(-t)+2*pow(y_prev, 3)*exp(-2*t))/2
            t += h
        print(f"h={h}, y={y}, error={exp(1)-y}")


if __name__ == "__main__":
    main()
