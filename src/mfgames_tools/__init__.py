"""Moonfire Games' Tools for Python"""


import argparse


def run_tool(descr, arguments, processes):
    """Runs the tools using the processes given as the argument."""

    # Set up the primary parser.
    parser = argparse.ArgumentParser(description=descr)

    # Go through the processes and add each one's subparser.
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
    selected_process = processes[selected_name]
    selected_process.process(args)
