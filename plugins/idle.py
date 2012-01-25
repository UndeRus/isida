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

idle_base = []

def idle(type, jid, nick, text):
	global idle_base
	if not len(text): text = nick
	msg = L('I can\'t find %s') % text
	for tmp in idle_base:
		if tmp[0] == jid and tmp[1] == text:
			if text == nick: msg = L('Your last activity was %s ago') % un_unix(int(time.time())-tmp[3])
			else: msg = L('%s\'s last ativity was %s ago') % (text, un_unix(int(time.time())-tmp[3]))
			if tmp[2] == 'm': msg += ' ('+L('message')+')'
			else: msg += ' ('+L('presence')+')'
			break
	send_msg(type, jid, nick, msg)

def append_to_idle(room,jid,nick,type,text):
	global idle_base
	for tmp in idle_base:
		if tmp[0] == room and tmp[1] == nick:
			idle_base.remove(tmp)
			break
	idle_base.append((room,nick,'m',int(time.time())))

def remove_from_idle(room,jid,nick,type,text):
	global idle_base
	for tmp in idle_base:
		if tmp[0] == room and tmp[1] == nick:
			idle_base.remove(tmp)
			break
	if type != 'unavailable': idle_base.append((room,nick,'p',int(time.time())))

global execute

message_control = [append_to_idle]
presence_control = [remove_from_idle]

execute = [(0, 'idle', idle, 2, L('Idle time'))]
