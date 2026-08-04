import socket
import sys
from datetime import datetime

SERVICOS_COMUNS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP (Web)",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS (Web Seguro)",
    445: "Microsoft-DS (SMB)",
    3306: "MySQL Database",
    3389: "Remote Desktop (RDP)",
    8080: "HTTP Proxy / Alt"
}

def exibir_cabecalho():
    print("-" * 60)
    print("      PYTHON NETWORK SCANNER - v2.0 (Portfólio)")
    print("-" * 60)

def main():
    exibir_cabecalho()

    if len(sys.argv) == 2:
        alvo_input = sys.argv[1]
    else:
        alvo_input = input("Digite o endereço IP ou host para escanear: ")

    try:
        alvo_ip = socket.gethostbyname(alvo_input)
    except socket.gaierror:
        print("\n[!] O hostname não pôde ser resolvido. Verifique o endereço.")
        sys.exit()

    print(f"\n[i] Alvo resolvido: {alvo_ip}")
    print(f"[i] Horário de início: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    inicio_tempo = datetime.now()
    portas_abertas = 0

    try:
        portas_para_escanear = sorted(SERVICOS_COMUNS.keys())
        
        for porta in portas_para_escanear:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            
            resultado = s.connect_ex((alvo_ip, porta))
            
            if resultado == 0:
                servico = SERVICOS_COMUNS.get(porta, "Desconhecido")
                print(f"[+] Porta {porta:<5} ({servico}) -> ABERTA")
                portas_abertas += 1
            
            s.close()

    except KeyboardInterrupt:
        print("\n\n[!] Varredura interrompida pelo usuário.")
        sys.exit()

    except socket.error:
        print("\n[!] Erro de conexão com a rede.")
        sys.exit()

    fim_tempo = datetime.now()
    tempo_total = fim_tempo - inicio_tempo

    print("-" * 60)
    print(f"[i] Varredura concluída.")
    print(f"[i] Total de portas abertas encontradas: {portas_abertas}")
    print(f"[i] Tempo total de execução: {tempo_total}")
    print("-" * 60)

if __name__ == "__main__":
    main()