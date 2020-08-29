def main():
    #rkf45()
    rkf12()


def rkf12():
    a, b = 0, 2  # endpoints
    y_0 = 0.5  # initial condition
    TOL = 10**-5  # tolerance
    hmin, hmax = 0.000001, 0.25  # min/max step sizes
    def f(t, y): return y-t**2+1

    print(f"TOL={TOL}")

    t, w, h = a, y_0, hmax
    FLAG = 1
    count = 1

    while FLAG:
        k1 = h*f(t, w)
        k2 = h*f(t+h, w+k1)

        R = 1/h*abs(k1-1/2*(k1+k2))

        if R <= TOL:
            t += h
            w += k1
            print(f"t={t}, w={w}, h={h}")
            count += 1

        d = 0.84*((TOL/R)**(1/4))
        if d <= 0.1:
            h /= 10
        elif d >= 4:
            h *= 4
        else:
            h *= d

        if h > hmax:
            h = hmax

        if t >= b:
            FLAG = 0
        elif t+h > b:
            h = b-t
        elif h < hmin:
            FLAG = 0
            print(f"minimum h exceeded (h={h})")

    print(f"count={count}")


def rkf45():
    a, b = 0, 2  # endpoints
    y_0 = 0.5  # initial condition
    TOL = 10**-5  # tolerance
    hmin, hmax = 0.01, 0.25  # min/max step sizes
    def f(t, y): return y-t**2+1

    t, w, h = a, y_0, hmax
    FLAG = 1
    count = 1

    while FLAG:
        k1 = h*f(t, w)
        k2 = h*f(t+1/4*h, w+1/4*k1)
        k3 = h*f(t+3/8*h, w+3/32*k1+9/32*k2)
        k4 = h*f(t+12/13*h, w+1932/2197*k1-7200/2197*k2+7296/2197*k3)
        k5 = h*f(t+h, w+439/216*k1-8*k2+3680/513*k3-845/4104*k4)
        k6 = h*f(t+1/2*h, w-8/27*k1+2*k2-3544/2565*k3+1859/4104*k4-11/40*k5)

        R = 1/h*abs(1/360*k1-128/4275*k3-2197/75240*k4+1/50*k5+2/55*k6)

        if R <= TOL:
            t += h
            w += 25/216*k1+1408/2565*k3+2197/4104*k4-1/5*k5
            print(f"t={t}, w={w}, h={h}")
            count += 1

        d = 0.84*((TOL/R)**(1/4))
        if d <= 0.1:
            h /= 10
        elif d >= 4:
            h *= 4
        else:
            h *= d

        if h > hmax:
            h = hmax

        if t >= b:
            FLAG = 0
        elif t+h > b:
            h = b-t
        elif h < hmin:
            FLAG = 0
            print(f"minimum h exceeded (h={h})")
    print(f"count={count}, fcount={fcount}")


if __name__ == "__main__":
    main()
