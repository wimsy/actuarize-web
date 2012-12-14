# -*- coding: utf-8 -*-

###############################################################################
#
# GetTeamByShortname
# Returns detailed information about one or more teams, using team shortnames.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTeamByShortname(Choreography):

    """
    Create a new instance of the GetTeamByShortname Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Teams/GetTeamByShortname')


    def new_input_set(self):
        return GetTeamByShortnameInputSet()

    def _make_result_set(self, result, path):
        return GetTeamByShortnameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTeamByShortnameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTeamByShortname
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTeamByShortnameInputSet(InputSet):
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
        Set the value of the TeamShortname input for this choreography. ((required, string) The Team shortname for which to return details.)
        """
        def set_TeamShortname(self, value):
            InputSet._set_input(self, 'TeamShortname', value)


"""
A ResultSet with methods tailored to the values returned by the GetTeamByShortname choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTeamByShortnameResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTeamByShortnameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTeamByShortnameResultSet(response, path)
