"""Moonfire Games' Tools for Python"""


import os
import argparse
import ConfigParser


def run_tool(
    descr,
    arguments,
    processes,
    config_id=None,
    config_dir_id=None):
    """Runs the tools using the processes given as the argument."""

    # Set up the primary parser.
    parser = argparse.ArgumentParser(description=descr)

    # If we have a configuration file id, then we want to try loading
    # that configuration file as defaults (or allow them to ignore
    # it).
    if config_id != None:
        # Add in the configuration file arguments.
        parser.add_argument(
            "--config", 
            metavar="FILE",
            help=("Uses the configuration file instead of searching "
                  + "the default locations"))
        parser.add_argument(
            "--no-config", 
            action="store_true",
            help=("Uses the configuration file instead of searching "
                  + "the default locations"))

        # Parse the initial arguments to get the configuration
        # file. Using parse_known_args will only parse the arguments
        # we are aware of (e.g., the configuration arguments).
        config_args, remaining_args = parser.parse_known_args()
        args = remaining_args

        # Load in the configuration file, optionally setting the
        # location or ignoring it entirely.
        load_config(config_id, config_dir_id, parser, config_args)

    # Go through the processes and add each one's subparser to the
    # current arguments.
    subparsers = parser.add_subparsers()

    for process_name, process in processes.iteritems():
        # Add this subparser to the primary parser.
        process_parser = subparsers.add_parser(
            process_name,
            help=process.get_help())
        process_parser.set_defaults(name=process_name)

        # Add the process-specific arguments to the parser.
        process.setup_arguments(process_parser)

    # Process the arguments given on the command line.
    args = parser.parse_args(arguments)

    # Use the default to figure out the process name which is then
    # used to call the process() method in that Process class.
    selected_name = args.name

    if not selected_name in processes:
        print "Unknown tool name: " + format(selected_name)
        exit(1)

    selected_process = processes[selected_name]
    selected_process.process(args)

def load_config(config_id, config_dir_id, parser, args):
    """Attempts to load configuration values into a file and add them
    to the default values for the parser."""

    # If we aren't parsing configuration files, don't do anything.
    if args.no_config:
        return

    # If we were provided a configuration file, we use it. Otherwise,
    # we look in the standard locations for the operation system we're
    # using.
    if args.config != None:
        config_locations = [args.config]
    else:
        # Figure out what the base name of the configuration will
        # be. For a file-based config, this will be either "config_id"
        # or ".config_id". For directory, it will be
        # "config_dir_id/config_id.ini" or
        # ".config_dir_id/config_id.ini". The individual calls will
        # add the "." as appropriate, so we just have to calculate the
        # name.
        if config_dir_id == None:
            config_path = config_id + ".ini"
        else:
            config_path = os.path.join(config_dir_id, config_id + ".ini")

        # Using the config_path, gather up all the locations we'll be
        # checking.
        config_locations = []
        config_locations += get_directory_config_locations(config_path)
        config_locations += get_home_config_locations(config_path)

    # Search the locations for the first file.
    for config_location in config_locations:
        #print "Trying: " + config_location

        # Check to see if the file exists.
        if os.path.isfile(config_location):
            # Load this file from the directory.
            ini = ConfigParser.SafeConfigParser()
            ini.read([config_location])
            defaults = dict(ini.items("Defaults"))

            # Load the defaults into the parser.
            parser.set_defaults(**defaults)

            # We are successful, so stop looking.
            return

def get_directory_config_locations(config_path):
    """Gets directory locations for the current working directory up
    to the root path."""

    # Get the current working directory.
    cwd = os.getcwd()

    # Add the path until we get every directory.
    paths = []

    while True:
        # Add this directory to the search path.
        paths += [
            os.path.join(cwd, config_path),
            os.path.join(cwd, "." + config_path),
            ]
        
        # Move up a level. If this returns None, we're done.
        new_cwd = os.path.dirname(cwd)

        if new_cwd == None or new_cwd == cwd:
            break

        cwd = new_cwd

    # Return the resulting path.
    return paths

def get_home_config_locations(config_path):
    # Use standard locations for the user profile based on the
    # operating system. This way, it shows up as ".config" for Linux
    # users and doesn't have the leading period for Windows users.
    if 'APPDATA' in os.environ:
        confighome = os.environ['APPDATA']
    elif 'XDG_CONFIG_HOME' in os.environ:
        confighome = os.environ['XDG_CONFIG_HOME']
    else:
        confighome = os.path.join(os.environ['HOME'], '.config')

    # Check the location with and without the period.
    return [
        os.path.join(confighome, config_path),
        ]
