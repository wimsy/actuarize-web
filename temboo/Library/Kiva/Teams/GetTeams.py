# -*- coding: utf-8 -*-

###############################################################################
#
# GetTeams
# Returns detailed information about one or more lending teams.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTeams(Choreography):

    """
    Create a new instance of the GetTeams Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Teams/GetTeams')


    def new_input_set(self):
        return GetTeamsInputSet()

    def _make_result_set(self, result, path):
        return GetTeamsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTeamsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTeams
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTeamsInputSet(InputSet):
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
        Set the value of the TeamID input for this choreography. ((required, string) A list of team IDs for which details are to be returned. Max list items: 20.)
        """
        def set_TeamID(self, value):
            InputSet._set_input(self, 'TeamID', value)


"""
A ResultSet with methods tailored to the values returned by the GetTeams choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTeamsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTeamsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTeamsResultSet(response, path)
