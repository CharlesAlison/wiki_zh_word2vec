#!/usr/bin/env python
# -*- coding: utf-8  -*-
#执行命令python 1_process.py C:\Users\Administrator\Desktop\wiki_zh_word2vec-master\zhwiki-latest-pages-articles.xml.bz2  wiki.zh.txt
#将xml的wiki数据转换为text格式
from __future__ import print_function

import logging
import os.path
import six
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 3:
        print("Using: python process_wiki.py enwiki.xxx.xml.bz2 wiki.en.text")
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = b" "
    i = 0

    output = open(outp, 'w', encoding="utf-8")
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        if six.PY3:
            # output.write(b' '.join(text).decode('utf-8') + '\n')
            output.write((' '.join(t for t in text)) + '\n')
        #   ###another method###
        #    output.write(
        #            space.join(map(lambda x:x.decode("utf-8"), text)) + '\n')
        else:
            output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")

# import logging
# import os.path
# import sys
#
# from gensim.corpora import WikiCorpus
#
# if __name__ == '__main__':
#     program = os.path.basename(sys.argv[0])#得到文件名
#     logger = logging.getLogger(program)
#
#     logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
#     logging.root.setLevel(level=logging.INFO)
#     logger.info("running %s" % ' '.join(sys.argv))
#
#     if len(sys.argv) < 3:
#         print (globals()['__doc__'] % locals())
#         sys.exit(1)
#
#     inp, outp = sys.argv[1:3]
#     space = " "
#     i = 0
#
#     output = open(outp, 'w')
#     wiki =WikiCorpus(inp, lemmatize=False, dictionary=[])#gensim里的维基百科处理类WikiCorpus
#     for text in wiki.get_texts():#通过get_texts将维基里的每篇文章转换位1行text文本，并且去掉了标点符号等内容
#         output.write(space.join(text) + "\n")
#         i = i+1
#         if (i % 10000 == 0):
#             logger.info("Saved "+str(i)+" articles.")
#
#     output.close()
#     logger.info("Finished Saved "+str(i)+" articles.")
#
#


