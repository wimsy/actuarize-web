# -*- coding: utf-8 -*-

###############################################################################
#
# Get
# Gets a specific child reference.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Get(Choreography):

    """
    Create a new instance of the Get Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Children/Get')


    def new_input_set(self):
        return GetInputSet()

    def _make_result_set(self, result, path):
        return GetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Get
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ChildID input for this choreography. ((required, string) The ID of the child.)
        """
        def set_ChildID(self, value):
            InputSet._set_input(self, 'ChildID', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the Fields input for this choreography. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the FolderID input for this choreography. ((required, string) The ID of the folder.)
        """
        def set_FolderID(self, value):
            InputSet._set_input(self, 'FolderID', value)

        """
        Set the value of the RefreshToken input for this choreography. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)


"""
A ResultSet with methods tailored to the values returned by the Get choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetResultSet(ResultSet):
        """
        Retrieve the value for the "NewAccessToken" output from this choreography execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        def get_NewAccessToken(self):
            return self._output.get('NewAccessToken', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetResultSet(response, path)
