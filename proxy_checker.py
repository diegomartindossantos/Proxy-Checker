import requests
import random
import socket



tmout = 5
lista_proxies = []
with open("proxies.txt","r+") as archivo:
    for x in archivo:
        x = x.replace("\n","")
        lista_proxies.append(x)

#lista_user_agents = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1","Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"]


#ip_pc_origen = socket.gethostbyname(socket.gethostname())
#print (f"ip origen {ip_pc_origen}")
        
def conexion():
    proxie_aleatorio = random.choice(lista_proxies)
    proxies_formateados = {
        "http":"http://"+proxie_aleatorio,
        "https":"http://"+proxie_aleatorio
    }
    try:
        r = requests.get("https://httpbin.org/ip",proxies=proxies_formateados, timeout=tmout)
        js = r.json()
        ip_post_proxy = js["origin"]
        proxie_aleatorio_sin_puerto = proxie_aleatorio.split(":")[0]
        if ip_post_proxy == proxie_aleatorio_sin_puerto:
            print (f"[OK]   -   Esperado: {proxie_aleatorio_sin_puerto}   Recibido: {ip_post_proxy}")
            lista_proxies.append(ip_post_proxy)
        else:
            print (f" [BAD]    -   Esperado: {proxie_aleatorio_sin_puerto}   Recibido: {ip_post_proxy}")
    except requests.ConnectTimeout:
        print (f"[ERROR]   -   ({proxie_aleatorio}) ConnectTimeout")
    except requests.exceptions.ProxyError:
        print (f"[ERROR]   -   ({proxie_aleatorio}) ProxyError")
    except requests.ConnectionError:
        print (f"[ERROR]   -   ({proxie_aleatorio}) ConnectionError")




tmout = int(input("TIMEOUT>> "))
for x in range(10):
    conexion()