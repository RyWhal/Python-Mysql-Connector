#!/usr/bin/env python2.6

"""
This is a bare bones script that establishes a connection to a MySQL database
and runs a query you define

This is just meant to be a skeleton for a jumping off point to do more fun things
with python+MySQL

Usage: mysqlConnection.py [-h HOST] [-d DATABASE] [-s SOCKET | --port PORT] -u USERNAME -p -q QUERY ...

Options:
--help                  you're looking at it.
-h --host HOSTNAME      Specify hostname [default: localhost].
-d --db DATABASE        Specify database [default: mysql].
-s --socket SOCKET      Specify socket.
-P --port PORT          Specify port [default: 3306].
-u --username USERNAME  Specify username.
-p --password           Password mode.
-q --query QUERY        Specify query.
"""

from docopt import docopt
from prettytable import PrettyTable
import sys
import getpass
import MySQLdb

def main(args):

	# variable imports from docopt arguments
	if args['--password']:
		password = getpass.getpass()
	query = ' '.join(args['--query'])
	hostname = args['--host']
	database = args['--db']
	port = args['--port']
	socket = args['--socket']
	username = args['--username']

	# need to cast port as an int to use in mysql connect
	port = int(port)

	# call the mysql_connect function and set the returned cursor object to 'cur'
	cur = mysql_connect(args, hostname, username, password, database, socket, port)

	# print out connection information and query
	print "hostname:", hostname
	if args['--db']:
		print "database:", database
	if args['--port']:
		print "port:", port
	if args['--socket']:
		print "socket:", socket
	print "query:", query

	# Add more fun logic and things here!
	# Maybe some QPS type fun?
	# Or compring some queries together?
	# Or perhaps get some troubleshooting information?
	# Woooooo Python!

	# this runs the specified query
	cur.execute(query)
	print "\n";

	#create a pretty table with all of the column names in the mysql results
	pt = PrettyTable([i[0] for i in cur.description])
	pt.align= "l"

	# fetch all of the rows from the query
	result = cur.fetchall ()

	# prints each row result into a pretty table
	for row in result:
		pt.add_row(row)

	print pt

# function to establish mysql connection
def mysql_connect(args, hostname, username, password, database, socket, port):
    # connect using port
    if args['--port']:
        db = MySQLdb.connect(host = hostname,
            user = username,
            passwd = password,
            db = database,
            port = port,
        )

    # connect using socket
    elif args['--socket']:
        db = MySQLdb.connect(host = hostname,
            user = username,
            passwd = password,
            db = database,
            socket = socket,
        )

    else:
        print "Socket or Port is required"

    # return db.cursor object to main
    return(db.cursor())

if __name__ == "__main__":
    sys.exit(
        main(docopt(__doc__))
    )
