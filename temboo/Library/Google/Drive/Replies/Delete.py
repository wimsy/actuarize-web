# -*- coding: utf-8 -*-

###############################################################################
#
# Delete
# Deletes a reply.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Delete(Choreography):

    """
    Create a new instance of the Delete Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Replies/Delete')


    def new_input_set(self):
        return DeleteInputSet()

    def _make_result_set(self, result, path):
        return DeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Delete
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

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
        Set the value of the CommentID input for this choreography. ((required, string) The ID of the comment.)
        """
        def set_CommentID(self, value):
            InputSet._set_input(self, 'CommentID', value)

        """
        Set the value of the FileID input for this choreography. ((required, string) The ID of the file.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)

        """
        Set the value of the RefreshToken input for this choreography. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the ReplyID input for this choreography. ((required, string) The ID of the reply.)
        """
        def set_ReplyID(self, value):
            InputSet._set_input(self, 'ReplyID', value)


"""
A ResultSet with methods tailored to the values returned by the Delete choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteResultSet(ResultSet):
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

class DeleteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteResultSet(response, path)
