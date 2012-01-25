#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
#                                                                             #
#    Plugin for iSida Jabber Bot                                              #
#    Copyright (C) 2012 Vit@liy <vitaliy@root.ua>                             #
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
# --------------------------------------------------------------------------- #

def train(type, jid, nick, text):
	try:
		from_to = map(lambda x: urllib.quote(x.encode('utf-8')), text.strip().split(' - '))
		url = 'http://rasp.yandex.ru/search/train/?fromName=%s&toName=%s' % (from_to[0], from_to[1])
		data = html_encode(load_page(url))
		res = re.findall('<a class="b-link" href="/thread/.+?><strong>(.+?)</strong> <span class="g-nowrap">(.+?)</span>.+?<span class="g-nowrap">(.+?)</span></a>.+?<strong>(.+?)</strong>.+?<strong>(.+?)</strong>.+?<div class="b-timetable__pathtime">\s+(.+?)<span class="b-timetable__mark">(.+?)</span>', data, re.I+re.S+re.U)
		if res.count(res[0]) > 1: res = res[:res.index(res[0], 1)]
		msg = '\n%s' % '\n'.join([u'%s\t%s-%s\t\t%s-%s\t(%s%s в пути)' % _ for _ in res])
		if not msg.strip() or 'b-pseudo-link js-transfers-trigger' in data: msg = L('What?')
	except:
		msg = L('Command execution error.')
	send_msg(type,jid,nick,msg)

global execute

execute = [(3, 'train', train, 2, L('Train schedules by Yandex. Example: train city1 - city2'))]