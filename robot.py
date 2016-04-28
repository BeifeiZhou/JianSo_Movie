__author__ = 'but0n'
from multiprocessing import Pool
from bs4 import BeautifulSoup
import time, random, requests, sqlite3
host = 'http://www.80s.tw'
def mLog(label):
    print('\033[0;32;31m[MASTER]\033[m: %s' % label)

def robLog(r_id, label, optColor = '\033[m'):
    print('\033[0;32;32m[ROBOT-%03d]\033[m: %s%s\033[m' % (r_id, optColor, label))

class domPa(object):
    def __init__(self, path, section = 'a', title = '.title', img = '.img', detail = '.detail'):
        self.path = path
        self.page = requests.get(host+path)
        self.status = self.page.status_code
        self.section = section
        self.img = img
        self.title = title
        self.detail = detail
        self.dom = BeautifulSoup(self.page.text, 'html.parser')
        self.p = Pool(5)

    def run(self):
        robLog(888, self.status)
        robLog(888, len(self.dom.select(self.section)))
        result = []
        for i,e in enumerate(self.dom.select(self.section)):
            if (e.get('title') and e.get('href')!='/'):
                result.append(self.p.apply_async(botTask,(i,e)))
                # self.botTask(i,e)
        self.p.close()
        self.p.join()
        for res in result:
            for e in res.get():
                dat = (e[0],e[1])
                db.execute('INSERT INTO movies VALUES(?,?)',dat)
        db.commit()


def botTask(i,e):
    robLog(i, 'Running...', '\033[0;36m')
    start = time.time()
    robLog(i, 'Jump to <%s>...' % e.get('title'))
    urll = host + e.get('href')
    pagee = requests.get(urll)
    dom = BeautifulSoup(pagee.text, 'html.parser')
    datas = []
    for ee in dom.select('span.xunlei')[0].select('a'):
        movieName = e.get('title')
        movieLink = ee.get('href')
        # saveData(movieName, movieLink)
        robLog(i, 'Got it ! [%s]@ %s' % (movieName, movieLink))
        datas.append([movieName,movieLink])
    end = time.time()
    robLog(i, 'Task done! Cost %0.2fs' % (end-start), '\033[0;36m')
    return (datas)

def saveData(name,link):
    db.execute("INSERT INTO movies VALUES(name,link)")
    db.commit()


mLog(u'but0n,I\'m Running!')
mLog('Connect Database...')
db = sqlite3.connect('mvv.db')
db.execute('CREATE TABLE movies(name text, link text primary key)')


if db:
    mLog('Succeed!')
i = 1
while i:
    i = i + 1
    bug = domPa('/movie/list/-----p'+str(i), 'a')
    if bug.status == 200:
        mLog('HTTP Connect Succeed! To [p%i]' % i)
        bug.run()
    else:
        mLog('Checkout your network!')
	i = 0


db.close()
mLog('DONE')
