#encoding='utf-8'
#an example by Steven Du, showing how to use this server for Chinese documents

# train: let the server learn the LSI model
# index: setup your own pool of documents that you want the query to search 
# find_similar : find the similar documents in the indexed pool of documents.
# Input to this server (train,index,find_similar) is a list of {'id': 'doc_%i' % num, 'tokens': text.split()}


from simserver import SessionServer
import codecs
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

serverFilePath='./temp_index_dir'

server = SessionServer(serverFilePath) # resume server (or create a new one)


texts=['如果 也 没有 的话 。 这个 确实 没有 办法 了 。 我 个人 建议您 重装 一遍 这个 软件 看看 是否 还是 一样 卸载 程序 里 也 没有 呢',
'我能 直接 删掉 这些 文件 吗 ？',
'不 建议 呢 。 因为 不 确定 这些 文件 中 是否 有 其他软件 的 文件 呢',
'好 的 ， 使用 看看 会断 么',
'它 只是 有时 自动 掉 ， 以后 看看 怎么样',
'这个 是 您 无线 驱动 ： http : / / driverdl . lenovo . com . cn / lenovo / driverfilesuploadfloder / 32228 / wlan _ win8 . 1 . exe',
'要是 问题 还是 出现 您 可以 安装 这个 试试',
'10 几个 版本 都 试过 了 么',
'目前 可以 确认 08 版本 以上 正常 运行',
'这个 是 电源 吧',
'http : / / weixin . lenovo . com . cn / img / files / user _ files / olhctjgaid22zzdnezguwbxzuxrq / voice / 16 _ 03 _ 17 / 1104209 _ 729724 _ 1458213046 . jpg',
'现在 不是 运行 问题 ， 是 安装 问题',
'点 电源 卸载 没 反应 呢',
'安装 有 什么 报错 么']


corpus=[{'id': 'doc_%i' % num, 'tokens': text.split()}
         for num, text in enumerate(texts)]


#One should use more data to train the lsi model
server.train(corpus, method='lsi')


#let just index the corpus
server.index(corpus)

#and find_similar for each documents, which should return itselft.

for s in corpus:
    print server.find_similar(s)
    
