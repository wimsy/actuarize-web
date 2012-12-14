# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecentLending
# Returns the 100 most recent loans made on Kiva by public lenders.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentLending(Choreography):

    """
    Create a new instance of the GetRecentLending Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/LendingActions/GetRecentLending')


    def new_input_set(self):
        return GetRecentLendingInputSet()

    def _make_result_set(self, result, path):
        return GetRecentLendingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentLendingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentLending
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentLendingInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentLending choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentLendingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentLendingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentLendingResultSet(response, path)
