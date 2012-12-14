# -*- coding: utf-8 -*-

###############################################################################
#
# GetGist
# Returns an individual gist with a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetGist(Choreography):

    """
    Create a new instance of the GetGist Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GistsAPI/Gists/GetGist')


    def new_input_set(self):
        return GetGistInputSet()

    def _make_result_set(self, result, path):
        return GetGistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetGistChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetGist
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetGistInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ID input for this choreography. ((required, string) The id for the gist you want to retrieve.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)


"""
A ResultSet with methods tailored to the values returned by the GetGist choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetGistResultSet(ResultSet):
        """
        Retrieve the value for the "Limit" output from this choreography execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        def get_Limit(self):
            return self._output.get('Limit', None)
        """
        Retrieve the value for the "Remaining" output from this choreography execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        def get_Remaining(self):
            return self._output.get('Remaining', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from GitHub.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetGistChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetGistResultSet(response, path)
