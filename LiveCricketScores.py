from bs4 import BeautifulSoup
import requests


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


r1 = requests.get("http://www.cricbuzz.com/cricket-match/live-scores")
soup = BeautifulSoup(r1.content, "html.parser")

data = soup.find_all("div", {"class": "cb-lv-main"})
matches = {}
ct = 0
print(bcolors.UNDERLINE+bcolors.HEADER+"All Matches"+bcolors.ENDC)
for inf in data:
    matches[ct] = inf.h3.text
    ct += 1
for sno in sorted(matches):
        print(bcolors.OKBLUE+'{}. {}'.format(sno+1, matches[sno])+bcolors.ENDC)
print("==========================")
choice = int(input(bcolors.BOLD+"Enter your choice: "+bcolors.ENDC))
print("==========================")
links = soup.find_all("div", {"class": "cb-schdl"})
lnk = {}
cnt = 0
for link in links:
    if cnt % 2 is 0:
        lnk[int(cnt/2)] = link.a["href"]
    cnt += 1
sorted(lnk)
search = lnk[choice]
r = requests.get("http://www.cricbuzz.com" + search)

soup = BeautifulSoup(r.content, "html.parser")
data1 = soup.find('div',{"ng-show":"isMiniscoreRendered"})
data = soup.find('div',{"class": "cb-col-scores"})
try:
    scr = data.find_all('div')
    cn = 0;
    print(bcolors.BOLD+bcolors.HEADER+"Score"+bcolors.ENDC)
    for scor in scr:
        if cn > 0:
            print(bcolors.OKGREEN+bcolors.BOLD+scor.text+bcolors.ENDC)
        cn += 1
    info = soup.find("div", {"class": "cb-min-inf"})
    try:
        stat = info.find_all('div')
        ct = 0
        inf = []
        for sts in stat:
            if ct % 7 != 0:
                inf.append(sts.text + " ")
            elif ct != 0:
                for i in inf:
                    if ct < 8:
                        print(bcolors.FAIL+i+bcolors.ENDC, end="")
                    else:
                        print(bcolors.OKBLUE+i+bcolors.ENDC, end="")
                print()
                inf.clear()
            ct += 1
        for i in inf:
            print(bcolors.OKBLUE+i+bcolors.ENDC, end="")
    except:
            dta = soup.find("div", {"class":"cb-min-stts"})
            print(dta.text)
            dta = soup.find("div", {"class": "cb-mom-itm"})
            print(dta.text)
            print(bcolors.FAIL+"Match Already ended"+bcolors.ENDC)
except:
    print(bcolors.FAIL+"Match not started yet"+bcolors.ENDC)














