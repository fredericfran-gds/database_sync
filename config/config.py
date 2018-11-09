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
        """
        function to initialize object but actual initialization
        happens when using the functions:
        1. create_from_config_file or
        2. create_from_args

        """
        pass

    def load_config_file(self, config):
        """
        function to set config parameters based on a YAML configuration file

        """
        self.parse(config)
        self.initialized = True

    @staticmethod
    def convert_args_to_args_map(args):
        """
        function to convert an object with attributes of the args to a map

        """

        args_map = map()
        args_map["db_type"] = args.db_type
        args_map["db_name"] = args.db_name
        args_map["backup"] = args.backup
        args_map["restore"] = args.restore
        args_map["s_type"] = args.s_type
        args_map["s_url"] = args.s_url
        args_map["tmp_path"] = args.tmp_path

        return args_map

    def load_args(self, args):
        """
        function to set the config parameters based on the inputs of this function

        """

        config_map = self.convert_args_to_args_map(args)
        self.validate(config_map)

    def parse(self, config):
        """
        function to parse a YAML configuration file

        """

        # TODO: implement the parsing of the configuration file.
        pass

    def validate(self, args_map):
        """
        function to validate a set of config parameters

        """

        err_string = ""
        if args_map["db_type"] not in self.db_choices:
            err_string += ": wrong database type selected {}".format(args_map["db_type"])

        if args_map["db_name"] == "":
            err_string += ": the database name cannot be empty"

        if args_map["backup"] == 1 & args_map["restore"] == 1:
            err_string += ": cannot do a backup and restore at same time"

        if args_map["backup"] == 0 & args_map["restore"] == 0:
            err_string += ": either a restore or a backup operation type must be specified"

        if args_map["s_type"] not in self.storage_types:
            err_string += ": wrong storage backend selected {}".format(args_map["s_type"])

        if args_map["s_url"] == "":
            err_string += ": the storage URL cannot be empty"

        if args_map["tmp_path"] == "":
            err_string += ": the temporary path cannot be empty"

        if err_string != "":
            raise ValueError("failed validation of input arguments{}".format(err_string))
