import requests
import threading
import sys
import os

os.system("clear")
def banner():
    print("""

\33[0;36m  ██████╗░░█████╗░████████╗░██████╗███████╗██████╗░
\33[0;36m  ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗
\33[0;36m  ██████╦╝██║░░██║░░░██║░░░╚█████╗░█████╗░░██████╔╝
\33[37;1m  ██╔══██╗██║░░██║░░░██║░░░░╚═══██╗██╔══╝░░██╔══██╗
\33[37;1m  ██████╦╝╚█████╔╝░░░██║░░░██████╔╝███████╗██║░░██║
\33[37;1m  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝

\033[1;99m [+] --------------------------------------------
\033[1;99m [+] Author     : canisMajor
\033[1;99m [+] Facebook   : facebook.com/dib_dr
\033[1;99m [+] Instagram  : instagram.com/dib_dr
\033[1;99m [+] --------------------------------------------
""")

def run(link, token):

    while True:

        headers = {

            'authority': 'graph.facebook.com',

            'cache-control': 'max-age=0',

            'sec-ch-ua-mobile': '?0',

            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',

        }

        try:

          response = requests.post(f'https://graph.facebook.com/me/feed?link={link}&published=0&access_token={token}', headers=headers)

          print(response.text)

        except:

          sys.exit()

def main():

    banner()

    print('\33[33;1m ┌───────────────────────────────────┐')
    #link = input('Link Posts : ')
    token = input(' ├──[•] Token Facebook : ')

   # token = input('Token FB : ')
    link = input(' ├──[•] Link Postingan : ')
    print(' └───────────────────────────────────┘')

    number_thread = int(input('Delay : (Default 5) '))

    for i in range(number_thread):
        thread = threading.Thread(target=run, args=(link, token))
        thread.start()

if __name__ == '__main__':

    main()
