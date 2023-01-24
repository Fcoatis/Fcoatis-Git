from calc import *
import functions_framework

@functions_framework.http
def main(request):
    calculo()
    return('Cálculo gerado com sucesso')