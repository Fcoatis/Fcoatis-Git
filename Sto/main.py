from read_fnames import *
import functions_framework

@functions_framework.http
def main(request):
    list_files()
    return('b3 historico sucesso')