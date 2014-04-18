Python-Mysql-Connector
======================

A basic Python that establishes a MySQL database connection and runs a query. It't meant as a skeleton file jump off point for further python/MySQL development

This script requires DocOpt (Pythonic command line arguments parser, that will make you smile http://docopt.org). Also check out their github page at https://github.com/docopt/docopt

Usage
=====

help page:
```
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
```

example usage:
```
~ % python mysqlConnection.py -h localhost -d information_schema --port 3306 -u ryan -p -q "select * from processlist limit 10"
Password:
hostname: localhost
database: information_schema
port: 3306
query: select * from processlist limit 10


835 ryan localhost
830 ryan localhost
```
