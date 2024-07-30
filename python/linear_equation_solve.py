def solve_linear_equation_with_one_l(equation: str) -> dict:
    """
    :param equation:
    :return:
    """
    if (len(equation.split("=")) == 2 and len(equation.split("=")[0]) != 0 and len(equation.split("=")[1]) != 0):
        # print("if work")
        left_side = equation.replace(" ", "").split("=")[0].replace("-", "+-").split("+")
        right_side = equation.replace(" ", "").split("=")[1].replace("-", "+-").split("+")
        return{
            "solution":[],
            "answer":""
        }
    else:
        return ({
            "kg": "Тендеме туура эмес жазылган!",
            "ru": "Неправильно введено уравнение",
            "en": "Wrong equation"
        })


print(solve_linear_equation_with_one_l(input("Введите уравнение: ")))
