# -*- coding: utf-8 -*-

###############################################################################
#
# GetLenderTeams
# Returns teams that a particular lender is part of.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLenderTeams(Choreography):

    """
    Create a new instance of the GetLenderTeams Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Lenders/GetLenderTeams')


    def new_input_set(self):
        return GetLenderTeamsInputSet()

    def _make_result_set(self, result, path):
        return GetLenderTeamsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLenderTeamsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLenderTeams
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLenderTeamsInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the LenderName input for this choreography. ((required, string) The lender name for which to return details.)
        """
        def set_LenderName(self, value):
            InputSet._set_input(self, 'LenderName', value)

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
A ResultSet with methods tailored to the values returned by the GetLenderTeams choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLenderTeamsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Kiva.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLenderTeamsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLenderTeamsResultSet(response, path)
