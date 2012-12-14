# -*- coding: utf-8 -*-

###############################################################################
#
# GetLenderDetails
# Returns details for lenders.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLenderDetails(Choreography):

    """
    Create a new instance of the GetLenderDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Lenders/GetLenderDetails')


    def new_input_set(self):
        return GetLenderDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetLenderDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLenderDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLenderDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLenderDetailsInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the LenderName input for this choreography. ((required, string) List of comma-delimited lender names for which to return details. Maximum list items: 50.)
        """
        def set_LenderName(self, value):
            InputSet._set_input(self, 'LenderName', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetLenderDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLenderDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLenderDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLenderDetailsResultSet(response, path)
