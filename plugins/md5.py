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

def md5body(type, jid, nick, text):
	if len(text): msg = hashlib.md5(text.encode('utf-8')).hexdigest()
	else: msg = L('What?')
	send_msg(type, jid, nick, msg)

def hashbody(type, jid, nick, text):
	if not len(text): text = nick
	try: msg = hashes['%s/%s' % (jid,text)]
	except: msg = L('Nick %s not found!') % text
	send_msg(type, jid, nick, msg)

global execute

execute = [(3, 'md5', md5body, 2, L('Calculate phrase md5 sum.')),
		   (4, 'hashbody', hashbody, 2, L('Show presence-hash of nick'))]
