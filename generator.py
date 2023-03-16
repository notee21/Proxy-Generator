import requests
from termcolor import colored
import time
import msvcrt

def get_proxies():

    bar = ['[      ]',
           '[=     ]',
           '[==    ]',
           '[===   ]',
           '[====  ]',
           '[===== ]',
           '[======]',
           '[ =====]',
           '[  ====]',
           '[   ===]',
           '[    ==]',
           '[     =]',
           '[      ]',
           '[=     ]',
           '[==    ]',
           '[===   ]']

    print("Processando", end="")
    for i in range(len(bar)):
        print('\rProcessando' + '' * len(bar) + bar[i], end='', flush=True)
        time.sleep(0.3)
    print("\n")

    url = "https://multiproxy.org/txt_all/proxy.txt"
    r = requests.get(url)
    proxy_list = r.text.split("\n")
    with open("proxies.txt", "w") as f:
        f.write("\n".join(proxy_list))
    print(f"Lista de {len(proxy_list)} proxies salva com sucesso em 'proxies.txt'.")

def create_box_text(text):
    # Adiciona o texto à caixa
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    boxed_text = ['╔' + '═' * (max_length + 2) + '╗']
    for line in lines:
        boxed_text.append('║ ' + line.ljust(max_length) + ' ║')
    boxed_text.append('╚' + '═' * (max_length + 2) + '╝')
    return '\n'.join(boxed_text)
# Cria a caixa de texto com as informações
text = '     ===========GET PROXY===========\n' \
       '          CODDED BY NOTE21\n' \
       '  Thanks To All Members Woll Cyber Team\n' \
       '     ==============================='
boxed_text = create_box_text(text)

get_proxies()

# Exibe a caixa de texto na tela
print(boxed_text)
print("Pressione qualquer tecla para fechar o programa")
msvcrt.getch()