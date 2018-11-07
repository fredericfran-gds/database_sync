#!/usr/bin/env python

"""
    This module defines the Config class which stores a configuration
    for a utility and has the ability to verify where a configuration
    is correct

"""


class Config(object):
    """
    Stores and validates the configuration

    """

    db_choices = ["postgresql", "mysql", "mongo", "elasticsearch"]
    storage_types = ["s3"]
    initialized = False

    def __init__(self):
        pass

    def create_from_config_file(self, config):
            self.parse(config)
            self.initialized = True

    def create_from_args(self, db_type,
                         db_name,
                         backup,
                         restore,
                         s_type,
                         s_url,
                         tmp_path,
                         timestamp):

        self.validate(db_type, db_name, backup, restore, s_type, s_url, tmp_path, timestamp)

    def parse(self, config):
        #TODO: implement the parsing of the configuration file.
        pass

    def validate(self, db_type,
                 db_name,
                 backup,
                 restore,
                 s_type,
                 s_url,
                 tmp_path,
                 timestamp):

        err_string = ""
        if db_type not in self.db_choices:
            err_string += ": wrong database type selected {}".format(db_type)

        if db_name == "":
            err_string += ": the database name cannot be empty"

        if backup == 1 & restore == 1:
            err_string += ": cannot do a backup and restore at same time"

        if backup == 0 & restore == 0:
            err_string += ": either a restore or a backup operation type must be specified"

        if s_type not in self.storage_types:
            err_string += ": wrong storage backend selected {}".format(s_type)

        if s_url == "":
            err_string += ": the storage URL cannot be empty"

        if tmp_path == "":
            err_string += ": the temporary path cannot be empty"

        #TODO find the logic for timestamp verification

        if err_string != "":
            raise ValueError("failed validation of input arguments{}".format(err_string))
