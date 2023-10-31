from math import sqrt
import matplotlib.pyplot as plt


def buildGraph(r=10, pointX=5, pointY=5, filename='plot.png'):
    X1, Y1 = [-r], [0]

    if r > 100:
        for x in range(int(-r)+1, int(r)):
            X1.append(x)
            Y1.append(sqrt(r**2 - x**2))
    else:
        delta = 100 if r > 10 else 1000

        tempR = r * delta
        
        for x in range(int(-tempR)+1, int(tempR)):
            X1.append(x / delta)
            Y1.append(sqrt(tempR**2 - x**2) / delta)

    X1.append(r), Y1.append(0)

    X1.append(-r), Y1.append(0)

    X2 = [0, 0, -r, 0]
    Y2 = [0, -r, -r, 0]

    ax = plt.gca()
    ax.axhline(y=0, color='black')
    ax.axvline(x=0, color='black')

    plt.plot(X1, Y1, X2, Y2, color='red')
    plt.fill_between(X1, Y1, color=(0, 0, 0, 0.3))
    plt.fill_between(X2, Y2, color=(0, 0, 0, 0.3))

    plt.plot(pointX, pointY, 'bo')

    plt.savefig(filename)
    
    plt.clf()

if __name__ == '__main__':
    buildGraph(r=9.2423423)