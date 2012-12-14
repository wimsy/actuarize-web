# -*- coding: utf-8 -*-

###############################################################################
#
# GetNewestLoans
# Returns a list of the most recent fundraising loans.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetNewestLoans(Choreography):

    """
    Create a new instance of the GetNewestLoans Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Loans/GetNewestLoans')


    def new_input_set(self):
        return GetNewestLoansInputSet()

    def _make_result_set(self, result, path):
        return GetNewestLoansResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewestLoansChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetNewestLoans
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetNewestLoansInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetNewestLoans choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetNewestLoansResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetNewestLoansChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNewestLoansResultSet(response, path)
