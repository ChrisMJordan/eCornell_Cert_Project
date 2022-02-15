"""
Module that validates the flight school's records.

This is the primary module that does all of the work. It loads the files, loops through
the lessons, and searches for any takeoffs that violate insurance requirements.

Technically, we could have put many of these functions in __main__.py.  That is the
main module of this application anyway.  However, for testing purposes we want all
functions in modules and we only want script code in the file __main__.py

Author: Christopher Jordan
Date: September 30, 2021
"""
import utils
import tests
import pilots
import os.path
import violations


# Uncomment for the extra credit
#import endorsements
#import inspections


def discover_violations(directory,output):
    """
    Searches the dataset directory for any flight lessons the violation regulations.

    This function will call list_weather_violations() to get the list of weather violations.
    If list_endorsment_violations (optional) is completed, it will call that too, as
    well as list_inspection_violations.  It will concatenate all of these 2d lists
    into a single 2d list of violations (so a flight may be listed more than once for
    each of the three types of violations).

    If the parameter output is not None, it will create the CSV file with name output
    and write the 2d list of violations to this file.  This CSV file should have the
    following header:

        STUDENT,AIRPLANE,INSTRUCTOR,TAKEOFF,LANDING,FILED,AREA,REASON

    Regardless of whether output is None, this function will print out the number of
    violations, as follows:

        '23 violations found.'

    If no violations are found, it will say

        'No violations found.'

    Parameter directory: The directory of files to audit
    Precondition: directory is the name of a directory containing the files 'daycycle.json',
    'weather.json', 'minimums.csv', 'students.csv', 'teachers.csv', 'lessons.csv',
    'fleet.csv', and 'repairs.csv'.

    Parameter output: The CSV file to store the results
    Precondition: output is None or a string that is a valid file name
    """

    vios = violations.list_weather_violations(directory)
    num_vios = len(vios)
    header = [['STUDENT', 'AIRPLANE', 'INSTRUCTOR', 'TAKEOFF', 'LANDING', 'FILED', 'AREA', 'REASON']]
    output_data = header + vios

    if len(vios) == 1:
        out_line = str(repr(num_vios)+' violation found.')
    elif len(vios) > 1:
        out_line = str(repr(num_vios)+' violations found.')
    elif len(vios) == 0:
        out_line = 'No violations found.'

    if output == None:
        filename = 'output.csv'
    elif output != None:
        filename = output

    utils.write_csv(output_data, filename)
    print(out_line)


def execute(args):
    """
    Executes the application or prints an error message if executed incorrectly.

    The arguments to the application (EXCLUDING the application name) are provided to
    the list args. This list should contain either 1 or 2 elements.  If there is one
    element, it should be the name of the data set folder or the value '--test'.  If
    there are two elements, the first should be the data set folder and the second
    should be the name of a CSV file (for output of the results).

    If the user calls this script incorrectly (with the wrong number of arguments), this
    function prints:

        Usage: python auditor dataset [output.csv]

    This function does not do much error checking beyond counting the number of arguments.

    Parameter args: The command line arguments for the application (minus the application name)
    Precondition: args is a list of strings
    """

    if len(args) == 0 or len(args) > 2:
        print('Usage: python auditor dataset [output.csv]')
    elif len(args) == 2 and args[1] == '--test':
        print('Usage: python auditor dataset [output.csv]')
    elif len(args) == 2 and args[0] == '--test':
        print('Usage: python auditor dataset [output.csv]')
    elif len(args) == 1 and args[0] == '--test':
        tests.test_all()
    else:
        try:
            if len(args) == 1:
                discover_violations(args)
            elif len(args) == 2:
                discover_violations(args[0], args[1])
        except:
            print('Usage: python auditor dataset [output.csv]')
