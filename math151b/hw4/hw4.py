import math
import numpy


def main():
    q2b()


def q2b():
    a, b, h = 0, 1, 0.1
    u0 = numpy.array([0, 0])

    def f(t, u):
        A = numpy.array([[0, 1], [4, 0]])
        b = numpy.array([0, 6*math.exp(-t)])
        return A.dot(u)+b

    def pred(f, wi, ti, h):
        return wi+h*f(ti+h/2, wi+h/2*f(ti, wi))

    def corr(f, wi, wi_bar, ti, h):
        return wi+h/2*f(ti, wi)+h/2*f(ti+h, wi_bar)

    steps = int((b-a)/h)
    wi = u0
    for i in range(steps):
        ti = (i-1)*h
        wi_bar = pred(f, wi, ti, h)
        wi = corr(f, wi, wi_bar, ti, h)

    print(f"y={wi[0]}, y'={wi[1]}")


if __name__ == "__main__":
    main()
