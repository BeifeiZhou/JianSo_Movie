# import sys, time, os
# detail = {'label' : 'NONE', 'url' : 'http://baidu.com', 'title':'none', 'detail':'none', 'link':'none', 'index':0, 'total':0}
# def mLog():
#     os.system('clear')
#     opt = detail
#     print('\033[41;30m MESSAGE: %s\033[m' % opt['label'])
#     print('\033[46;30m PATH: %10s\033[m\n' % opt['url'])
#
#     print('\033[0;35m TITLE\033[m:\t%s' % opt['title'])
#     print('\033[0;34m DETAIL\033[m:%s' % opt['detail'])
#     print('\033[0;36m LINK\033[m:\t%s' % opt['link'])
#
#     bar_status = opt['index']*40/opt['total']
#     status = opt['index']*100/opt['total']
#     print('\n[%-40s]%s(%d/%d)' % ('>'*bar_status, str(status)+'%', opt['index'], opt['total']))
# for i in range(80):
#     detail['url']
#     detail['total']=79
#     detail['index']=i
#     mLog()
#     time.sleep(0.09)
import multiprocessing

def f(n, a):
    n.value   = 3.14
    a[-1]      = 5

num   = multiprocessing.Value('d', 0.0)
arr   = multiprocessing.Array(7,['NONE', 'http://baidu.com', 'title', 'detail', 'link', 0, 0])

p = multiprocessing.Process(target=f, args=(num, arr))
p.start()
p.join()

print num.value
print arr[:]
