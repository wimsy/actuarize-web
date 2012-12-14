# -*- coding: utf-8 -*-

###############################################################################
#
# ByTwitterID
# Performs a lookup for a user's identity using a Twitter ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByTwitterID(Choreography):

    """
    Create a new instance of the ByTwitterID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Klout/Identity/ByTwitterID')


    def new_input_set(self):
        return ByTwitterIDInputSet()

    def _make_result_set(self, result, path):
        return ByTwitterIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByTwitterIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByTwitterID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByTwitterIDInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Klout.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the TwitterID input for this choreography. ((required, integer) The numeric ID for a Twitter user.)
        """
        def set_TwitterID(self, value):
            InputSet._set_input(self, 'TwitterID', value)


"""
A ResultSet with methods tailored to the values returned by the ByTwitterID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByTwitterIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Klout.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByTwitterIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByTwitterIDResultSet(response, path)
