#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
#                                                                             #
#    Plugin for iSida Jabber Bot                                              #
#    Copyright (C) 2012 diSabler <dsy@dsy.name>                               #
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

def known(type, jid, nick, text):
	text = text.strip()
	if text == '': text = nick
	mdb = sqlite3.connect(agestatbase,timeout=base_timeout)
	cu = mdb.cursor()
	real_jid = cu.execute('select jid from age where room=? and (nick=? or jid=?)',(jid,text,text.lower())).fetchone()
	if real_jid:
		nicks = cu.execute('select nick from age where room=? and jid=?',(jid,real_jid[0])).fetchall()
		if text == nick: msg = L('I know you as:') + ' '
		else: msg = L('I know %s as:') % text + ' '
		for tmp in nicks:
			msg += tmp[0] + ', '
		msg = msg[:-2]
	else: msg = L('Not found!')
	send_msg(type, jid, nick, msg)

global execute

execute = [(3, 'known', known, 2, L('Show user\'s nick changes.'))]
