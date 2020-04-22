# Task 7 | CIS 223 | Spring 2020
# Author: Colin Roskos
#


def number_steps_lin(n):
    if n < 0:
        raise ValueError
    sol = [0, 1, 2, 4]
    if n < 4:
        return sol[n]
    for index in range(4, n+1):
        if index == len(sol):
            sol.append(sol[index-1] + sol[index-2] + sol[index-3])

    return sol[-1]


def number_steps_expo(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    sum = 0
    sum += number_steps_lin(n-1)
    sum += number_steps_lin(n-2)
    sum += number_steps_lin(n-3)
    return sum


def main():
    print(number_steps_lin(1))
    print(number_steps_lin(2))
    print(number_steps_lin(3))
    print(number_steps_lin(4))
    print(number_steps_lin(5))
    print(number_steps_lin(6))
    print(number_steps_lin(7))
    print(number_steps_lin(8))
    print(number_steps_lin(9))
    print(number_steps_lin(10))
    print(number_steps_lin(11))
    print(number_steps_lin(12))




if __name__=='__main__':
    main()