#!/usr/bin/env python

import argparse
import logging

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

ProgramName = "Database Sync Utility"


def validateArgs(args):



def getArgs():
    parser = argparse.ArgumentParser(prog='{}'.format(ProgramName),
                                     description='This utility allows databases to be restored or backed up')

    parser.add_argument("-c, --config_file",
                        help="configuration file which configures this utility", dest="configFile")
    parser.add_argument("-d, --db_type", choices= DBChoices, required=True,
                        help="type of database to be restored or backed up", dest="dbType")
    parser.add_argument("-n, --db_name", required=True,
                        help="name of database to be restored or backed up", dest="dbName")
    parser.add_argument("-b, --backup", help="back-ups database", dest="backup", action='store_true')
    parser.add_argument("-r, --restore", help="restores database", dest="restore", action='store_true')
    parser.add_argument("-s, --storage", choices=StorageTypes, required=True,
                        help="type of backend used to backup or restore database", dest="sType")
    parser.add_argument("-u, --s_url", required=True,
                        help="url inside the storage scope", dest="sURL")
    parser.add_argument("-p, --tmp_path", required=True,
                        help="temporary path to create directory", dest="tmpPath")
    parser.add_argument("-t, --timestamp", required=True,
                        help="timestamp to be applied", dest="timestamp")

    args = parser.parse_args()

    #print "database type: {}, backup: {}, restore: {}, {}".format(args.dbType, args.backup, args.restore, type(args))
    validateArgs(args)


if __name__ == "__main__":
    logging.info("Starting {}...".format(ProgramName))
    getArgs()
