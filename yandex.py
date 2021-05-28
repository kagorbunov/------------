class Robot(hod=()):
    long = ""
    x = hod[0]
    y = hod[1]
    n = hod[0]
    m = hod[1]

    def move(self,a):
        d = len(a)
        for i in range(d):
            if a[i] == N:
                y += 1
                long += "N"
                hod[1] += 1
            elif a[i] == E:
                x += 1
                hod[0] += 1
                long += "E"
            elif a[i] == S:
                y -= 1
                hod[1] -= 1
                long += "S"
            elif a[i] == W:
                x -= 1
                hod[0] -= 1
                long += "W"
        return hod;


    def path(self):
        for i in range(long):
            if long[i] == N:
                m += 1
                return (n, m)
            elif long[i] == E:
                n += 1
                return (n, m)
            elif long[i] == S:
                m -= 1
                return (n, m)
            elif long[i] == W:
                n -= 1
                return (n, m)
            else:
                return (n, m)

r = Robot((0,0))
print(r.move('NENW'))
print(*r.path())
