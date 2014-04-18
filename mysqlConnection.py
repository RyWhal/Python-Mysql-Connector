#!/usr/bin/env python2.6

"""
This is a bare bones script that establishes a connection to a MySQL database
and runs a query you define

This is just meant to be a skeleton for a jumping off point to do more fun things
with python+MySQL

Usage: mysqlConnection.py [-h HOST] [-d DATABASE] [-s SOCKET | --port PORT] -u USERNAME -p [-f FILTER] -q QUERY ...

Options:
--help                  you're looking at it.
-h --host HOSTNAME      Specify hostname [default: localhost].
-d --db DATABASE        Specify database [default: mysql].
-s --socket SOCKET      Specify socket.
-P --port PORT          Specify port [default: 3306].
-u --username USERNAME  Specify username.
-p --password           Password mode.
-f --filter FILTER      Specify filter.
-q --query QUERY        Specify query.
"""

from docopt import docopt
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
    filter = args['--filter']

    # need to cast port as an int to use in mysql connect
    port = int(port)

    # call the mysql_connect function and set the returned cursor object to 'cur'
    cur = mysql_connect(args, hostname, username, password, database, socket, port)

    # print out connection information and query
    print "hostname:", hostname
    print "database:", database
    if args['--port']:
        print "port:", port
    if args['--socket']:
        print "socket:", socket
    if args['--filter']:
        print "filter:", filter
    print "query:", query


    # Add more fun logic and things here!
    # Maybe some QPS type fun?
    # Or compring some queries together?
    # Or perhaps get some troubleshooting information?
    # Woooooo Python!

    # this runs the specified query
    cur.execute(query)
    print "\n";
    
    # fetch all of the rows from the query
    result = cur.fetchall ()

    # pulls out columns 1, 2 and 3 from each row
    # This requires a little TLC to make it work to your needs
    #this is just a basic exmaple of how to get back your data
    for row in result:
        print row[0], row[1], row[2]    

# function to establish mysql connection using either port or socket
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
