# -*- coding: utf-8 -*-

###############################################################################
#
# LocalBreakdown
# Returns a breakdown of how much of the money raised was from contributors in the politician's state versus outside the politician's state.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LocalBreakdown(Choreography):

    """
    Create a new instance of the LocalBreakdown Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/LocalBreakdown')


    def new_input_set(self):
        return LocalBreakdownInputSet()

    def _make_result_set(self, result, path):
        return LocalBreakdownResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LocalBreakdownChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LocalBreakdown
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LocalBreakdownInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Sunlight Data Services.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EntityID input for this choreography. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)


"""
A ResultSet with methods tailored to the values returned by the LocalBreakdown choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LocalBreakdownResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Influence Explorer.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LocalBreakdownChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LocalBreakdownResultSet(response, path)
