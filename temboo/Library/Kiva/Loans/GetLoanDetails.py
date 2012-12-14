# -*- coding: utf-8 -*-

###############################################################################
#
# GetLoanDetails
# Returns detailed information for multiple loans.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLoanDetails(Choreography):

    """
    Create a new instance of the GetLoanDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Loans/GetLoanDetails')


    def new_input_set(self):
        return GetLoanDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetLoanDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLoanDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLoanDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLoanDetailsInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the LoanID input for this choreography. ((required, string) A comma-delimited list of the loan IDs for which to get details. Maximum list items: 10.)
        """
        def set_LoanID(self, value):
            InputSet._set_input(self, 'LoanID', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetLoanDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLoanDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLoanDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLoanDetailsResultSet(response, path)
