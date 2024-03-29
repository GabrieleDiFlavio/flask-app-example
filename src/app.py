import sys
from io import StringIO
from gmpy2 import xmpz,div,mul,add
import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def computepi(N=10):
    f = StringIO()
    w = xmpz(0)
    k = 1
    n1 = xmpz(4)
    n2 = xmpz(3)
    d = xmpz(1)
    f10 = xmpz(10)
    n10 = xmpz(-10)
    i = 0

    while True:
        # digit
        u = int(div(n1,d))
        v = int(div(n2,d))
        if u == v:
            f.write(chr(48+u))
            i += 1
            if i % 10 == 0:
                f.write("\t:%d\n" % i)

            if i == N:
                break

            # extract
            u  = mul(d, mul(n10, u))
            n1 = mul(n1, f10)
            n1 = add(n1, u)
            n2 = mul(n2, f10)
            n2 = add(n2, u)
        else:
            # produce
            k2 = k << 1
            u  = mul(n1, k2 - 1)
            v  = add(n2, n2)
            w  = mul(n1, k - 1)
            n1 = add(u, v)
            u  = mul(n2, k + 2)
            n2 = add(w, u)
            d  = mul(d, k2 + 1)
            k += 1;
    return(f.getvalue())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    startDownload = time.time() * 1000.0
    result = computepi(2000)
    stopDownload = time.time() * 1000.0
    delay = stopDownload - startDownload
    print("Execution time '" + str(delay) + "(ms)")

