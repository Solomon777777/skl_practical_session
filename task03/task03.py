from typing import Any

'''
def func(var, value, a = 5, b = 7, c = 3, d = 2):
	res = int(a * (value ** 3) - b * (value ** 2) - c * value + d)
	if a > 3 or b < 2:
		pass
	else:
		var.write(int(a / b))
	if c > 2 and d > 0:
		try:
			var.write(int(value / (d // c)))
		except Exception as e:
			var.write("A fost intalnita o exceptie" + "\n")
	if a ** d == 25:
		var.write(str(a ** c))

	var.write(str(a * b + c * d) + "\n")
	return res


if __name__ == '__main__':
	name = str(input())
	value = int(input())
	var = open(name, "w+")
	res = func(var, value)
	var.write(str(value) + "\n")
	var.close()
	

	'''
def func(var, value, a=5, b=7, c=3, d=2):
    res = a * (value ** 3) - b * (value ** 2) - c * value + d
    if a > 3 and b < 2:
        var.write(str(a / b))
    if c > 2 and d > 0:
        try:
            var.write(str(value / (d // c)))
        except Exception as e:
            var.write("A fost intalnita o exceptie" + "\n")
    if a ** d == 25:
        var.write(str(a ** c))
    var.write(str(a * b + c * d) + "\n")
    return res


if __name__ == '__main__':
    print("Please enter a filename:")
    name = str(input())
    print("Please enter a integer value:")
    value = int(input())
    try:
        with open(name, "w+") as var:
            res = func(var, value)
            var.write(str(value) + "\n")
    except Exception as e:
        print("A fost intalnita o exceptie: ", str(e))



