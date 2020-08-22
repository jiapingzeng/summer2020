from math import pow
from matplotlib import pyplot


def main():
    q3()


def q3():
    def f(t, w): return pow(t, 2)-1
    exact_val = -2/3
    h_vals = [pow(2, -n) for n in range(0, 10)]
    t_0, t_f, y_0 = 0, 1, 0
    graph_x, graph_y = [], []

    print("(Euler's method)")
    for h in h_vals:
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        for _ in range(steps):
            y_prev = y
            y = y_prev + h*f(t, y_prev)
            t += h
        print(f"h={h}, y={y}, error={abs(y-exact_val)}")
        graph_x.append(h)
        graph_y.append(abs(y-exact_val))
    pyplot.plot(graph_x, graph_y, label="Euler's method")
    graph_x.clear()
    graph_y.clear()

    print("(Modified Euler's method)")
    for h in h_vals:
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        for _ in range(steps):
            y_prev = y
            y = y_prev + h/2*(f(t, y_prev)+f(t+h, y_prev+h*f(t, y_prev)))
            t += h
        print(f"h={h}, y={y}, error={abs(y-exact_val)}")
        graph_x.append(h)
        graph_y.append(abs(y-exact_val))
    pyplot.plot(graph_x, graph_y, label="Modified Euler's method")
    graph_x.clear()
    graph_y.clear()

    print("(Heun's method)")
    for h in h_vals:
        t, y, steps = t_0, y_0, int((t_f-t_0)/h)
        for _ in range(steps):
            y_prev = y
            y = y_prev + h/4*(f(t, y_prev)+3*f(t+2*h/3,
                y_prev+2*h/3*f(t+h/3, y_prev+h/3*f(t, y_prev))))
            t += h
        print(f"h={h}, y={y}, error={abs(y-exact_val)}")
        graph_x.append(h)
        graph_y.append(abs(y-exact_val))
    pyplot.plot(graph_x, graph_y, label="Heun's method")
    graph_x.clear()
    graph_y.clear()

    pyplot.xlim(1, 0)
    pyplot.xlabel("Step size")
    pyplot.ylabel("Approximation error")
    pyplot.legend()
    pyplot.show()


def q17b():
    r, b = 0.1, 0.02
    t_0, t_f, y_0, h = 0, 50, 0.01, 1
    def f(t, w): return r*b*(1-w)

    t, y, steps = t_0, y_0, int((t_f-t_0)/h)
    for _ in range(steps):
        y_prev = y
        y = y_prev + h/4*(f(t, y_prev)+3*f(t+2*h/3,
            y_prev+2*h/3*f(t+h/3, y_prev+h/3*f(t, y_prev))))
        t += h
    print(f"y={y}")


if __name__ == "__main__":
    main()
