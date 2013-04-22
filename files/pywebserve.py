# pywebserve - A very simple pytho-based webserver.
#
# Copyright (c) 2013 Fabian Affolter <fabian@affolter-engineering.ch>
#
# All rights reserved.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# 
import os
import BaseHTTPServer
import SimpleHTTPServer

def main():
    datastore = os.chdir('/var/www/')
    port = 8880
    server_class  = BaseHTTPServer.HTTPServer
    handler_class = SimpleHTTPServer.SimpleHTTPRequestHandler
    server_address = ('', port)
    server = server_class(server_address, handler_class)
    server.serve_forever()

if __name__ == "__main__":
    main()
