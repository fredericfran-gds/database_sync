#!/usr/bin/env python

"""
Entry point to the Database Sync Utility
"""


import argparse
import logging
from config.config import Config

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

PROGRAM_NAME = "Database Sync Utility"


def validate_args(args):
    """
    function to validate args and get a config back
    """
    new_config = Config()

    if args.config_file is not None:
        new_config.load_config_file(args.config_file)
    else:
        new_config.load_args(args)


def get_args():
    """
    function to retrieve command arguments from the command line
    """

    parser = argparse.ArgumentParser(prog='{}'.format(PROGRAM_NAME),
                                     description=
                                     'This utility allows databases to be restored or backed up')
    parser.add_argument("-c", "--config_file",
                        help="configuration file which configures this utility", dest="config_file")
    parser.add_argument("-d", "--db_type", choices=Config.db_choices,
                        help="type of database to be restored or backed up", dest="db_type")
    parser.add_argument("-n", "--db_name",
                        help="name of database to be restored or backed up", dest="db_name")
    parser.add_argument("-b", "--backup", help="back-ups database", dest="backup",
                        action='store_true')
    parser.add_argument("-r", "--restore", help="restores database", dest="restore",
                        action='store_true')
    parser.add_argument("-s", "--storage", choices=Config.storage_types,
                        help="type of backend used to backup or restore database", dest="s_type")
    parser.add_argument("-u", "--s_url",
                        help="url inside the storage scope", dest="s_url")
    parser.add_argument("-p", "--tmp_path",
                        help="temporary path to create directory", dest="tmp_path")

    args = parser.parse_args()

    # print "database type: {}, backup: {}, restore: {}, {}".
    # format(args.dbType, args.backup, args.restore, type(args))
    validate_args(args)


if __name__ == "__main__":
    logging.info("Starting %s...", PROGRAM_NAME)
    get_args()
