
# a = float(input(Lado 1: ))
# b = float(input(Lado 2: ))
# c = float(input(Lado 3: ))
# #| b - c | < a < b + c
# if abs(b - c) < a and a < b + c):
#     #| a - c | < b < a + c
#     if abs(a - c) < b and b < a + c:
#         #| a - b | < c < a + b
#         if abs(a - b) < c and c < a + b:
#             p = (a + b + c)/2
#             # área dada pela fórmula de Heron
#             area = (p * (p - a) * (p - b) * (p - c))**(1/2)
#             print('Área é: ', area)
#         else:
#             print('Triângulo impossível')
#     else:
#         print('Triângulo impossível')
# else:
#     print('Triângulo impossível')



# a = float(input(Lado 1: ))
# b = float(input(Lado 2: ))
# c = float(input(Lado 3: ))
# #| b - c | < a < b + c
# if (abs(b - c) < a and a < b + c) 
#     and (abs(a - c) < b and b < a + c)
#     and (abs(a - b) < c and c < a + b) ):
#             p = (a + b + c)/2
#             # área dada pela fórmula de Heron
#             area = (p * (p - a) * (p - b) * (p - c))**(1/2)
#             print('Área é: ', area)
# else:
#     print('Triângulo impossível')

def validar(a, b, c):
    if abs(b - c) < a and a < b + c:
        return True
    else:
        return False

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))
if validar(a, b, c) and validar(b, a, c) and validar(c, b, a):
    p = (a + b + c)/2
    # área dada pela fórmula de Heron
    area = (p * (p - a) * (p - b) * (p - c))**(1/2)
    print('Área é: ', area)
else:
    print('O triângulo é impossível')
