from gera_pdf import *
import functions_framework

@functions_framework.http
def main(request):
    gerar_pdf()
    return('pdf gerado com sucesso')