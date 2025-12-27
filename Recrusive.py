def func1(n):
    if n == 0:
        return
    func1(n - 1)

def func2(n):
    if n == 0:
        return
    func2(n - 1)
    func2(n - 1)

func1(5)
func2(3)
