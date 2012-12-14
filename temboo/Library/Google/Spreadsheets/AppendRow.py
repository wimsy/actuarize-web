# -*- coding: utf-8 -*-

###############################################################################
#
# AppendRow
# Appends a simple comma-separated row of data to a given Google Spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AppendRow(Choreography):

    """
    Create a new instance of the AppendRow Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/AppendRow')


    def new_input_set(self):
        return AppendRowInputSet()

    def _make_result_set(self, result, path):
        return AppendRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AppendRowChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AppendRow
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AppendRowInputSet(InputSet):
        """
        Set the value of the RowData input for this choreography. ((required, string) A comma separated list of items to be added as a new row to the spreadsheet.)
        """
        def set_RowData(self, value):
            InputSet._set_input(self, 'RowData', value)

        """
        Set the value of the Password input for this choreography. ((required, password) Your Google password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SheetName input for this choreography. ((optional, string) The name of the sheet to write to. If not specified, rows are written to the first sheet.)
        """
        def set_SheetName(self, value):
            InputSet._set_input(self, 'SheetName', value)

        """
        Set the value of the SpreadsheetTitle input for this choreography. ((required, string) The title of the spreadsheet that you want to write rows to.)
        """
        def set_SpreadsheetTitle(self, value):
            InputSet._set_input(self, 'SpreadsheetTitle', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the AppendRow choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AppendRowResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Returns the string "success" if no error occurs.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AppendRowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AppendRowResultSet(response, path)
