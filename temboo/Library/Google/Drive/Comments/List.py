# -*- coding: utf-8 -*-

###############################################################################
#
# List
# Lists a file's comments.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class List(Choreography):

    """
    Create a new instance of the List Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Comments/List')


    def new_input_set(self):
        return ListInputSet()

    def _make_result_set(self, result, path):
        return ListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the List
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListInputSet(InputSet):
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
        Set the value of the Fields input for this choreography. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the FileID input for this choreography. ((required, string) The ID of the file.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)

        """
        Set the value of the IncludeDeleted input for this choreography. ((optional, boolean) If set, this will succeed when retrieving a deleted comment, and will include any deleted replies. (Default: false))
        """
        def set_IncludeDeleted(self, value):
            InputSet._set_input(self, 'IncludeDeleted', value)

        """
        Set the value of the MaxResults input for this choreography. ((optional, string) The maximum number of discussions to include in the response, used for paging. Acceptable values are 0 to 100, inclusive. (Default: 20))
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the PageToken input for this choreography. ((optional, string) The continuation token, used to page through large result sets. To get the next page of results, set this parameter to the value of "nextPageToken" from the previous response.)
        """
        def set_PageToken(self, value):
            InputSet._set_input(self, 'PageToken', value)

        """
        Set the value of the RefreshToken input for this choreography. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the UpdatedMIn input for this choreography. ((optional, string) Only discussions that were updated after this timestamp will be returned. Formatted as an RFC 3339 timestamp.)
        """
        def set_UpdatedMIn(self, value):
            InputSet._set_input(self, 'UpdatedMIn', value)


"""
A ResultSet with methods tailored to the values returned by the List choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListResultSet(ResultSet):
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

class ListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListResultSet(response, path)
