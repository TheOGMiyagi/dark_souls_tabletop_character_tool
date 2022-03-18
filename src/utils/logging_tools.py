import logging

def acknowledge_import(**kwargs):

    """<Method "Project/[__name__]._acknowledge_import()">

    Description:

        This module method is intended to be used at the end of the "if __name__ == '__main__':" idiom.

        Its purpose is to provide dynamic functionality to the very simple task that is this method's namesake.

        

    Args:

        output_method (method, optional):  Allows for the caller to specify the method to which the output is pipelined. Defaults to `logging.debug`.

        name_type (str, optional):     Allows for the caller to specify whether the name is the full path or module name. Defaults to 'full path'.

        docstring (bool, optional):     Allows for the caller to disable module docstrings in the output. Defaults to True.

    """

    _logging_types = [logging.debug, logging.info, logging.warning, logging.error]

    #? Assigns local internal variables from the keyword arguments.

    _output_method = kwargs.get('output_method', logging.debug)

    _full_path:  str= kwargs.get('full_path', 'full path')

    _docstring: bool = kwargs.get('docstring', True)

    try:

        #? Handles the output name for the module based on `full_path`

        if _full_path:

            _name = __name__

            _output = "%s was successfully imported." % _name

        else:

            _name = __name__.split(".")

            _output = "%s was successfully imported." % _name[-1]

        #? Handles Docstring based on `docstring`

        if _output_method not in _logging_types and _docstring and __doc__:

            _output += "\n%s" % __doc__

        #? Handles output based on `output_method`

        if _output_method in _logging_types or _output_method is print:

            _output_method(_output)

        else:

            raise TypeError("_output_method Error: Must be the print function or a logging mode.")

    except TypeError as e:

        logging.error(e)

        print(e)

