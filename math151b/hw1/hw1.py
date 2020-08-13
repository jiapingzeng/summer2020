def main():
    q2b()


def q2b():
    h_vals = [0.5, 0.2, 0.1, 0.01]  # step sizes
    t_0, y_0, t_f = 1.0, 2.0, 2.0  # initial/final values

    for h in h_vals:
        print(f"h={h}")
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        for _ in range(steps):
            y_prev = y
            y = y_prev + h*(1+t)/(1+y_prev)
            t += h
        print(f"y={y}\n")


if __name__ == "__main__":
    main()
