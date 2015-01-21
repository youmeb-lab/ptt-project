#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nsq
from ptt_crawler import Board


def fetch_list(board_name, nsqd='127.0.0.1:4150', stop=None):
    '''抓取文章連結、丟 queue

    Options:
        --stop=<string>   終止文章網址/ID
        --nsqd=<string>
    '''

    board = Board(board_name)
    writer = nsq.Writer([nsqd])
    topic = 'ptt:' + board_name

    for article in board.articles():
        writer.pub(topic, article.path)


if __name__ == '__main__':
    import clime.now
