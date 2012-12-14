# -*- coding: utf-8 -*-

###############################################################################
#
# Get
# Gets a file's metadata and content by ID.
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
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Files/Get')


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
        Set the value of the ExportFormat input for this choreography. ((optional, string) Indicates the download format (i.e. pdf, doc, txt, rtf, odt, etc). When specified, the FileContent output will contain the file's base64 encoded value.)
        """
        def set_ExportFormat(self, value):
            InputSet._set_input(self, 'ExportFormat', value)

        """
        Set the value of the Fields input for this choreography. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the FileID input for this choreography. ((required, string) The ID of the file to retrieve.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)

        """
        Set the value of the RefreshToken input for this choreography. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the UpdateViewDate input for this choreography. ((optional, boolean) Whether to update the view date after successfully retrieving the file. Default value is false.)
        """
        def set_UpdateViewDate(self, value):
            InputSet._set_input(self, 'UpdateViewDate', value)


"""
A ResultSet with methods tailored to the values returned by the Get choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetResultSet(ResultSet):
        """
        Retrieve the value for the "FileContent" output from this choreography execution. ((string) The Base64 encoded file content.)
        """
        def get_FileContent(self):
            return self._output.get('FileContent', None)
        """
        Retrieve the value for the "FileMetadata" output from this choreography execution. ((json) The file metadata returned in the response from Google.)
        """
        def get_FileMetadata(self):
            return self._output.get('FileMetadata', None)
        """
        Retrieve the value for the "NewAccessToken" output from this choreography execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        def get_NewAccessToken(self):
            return self._output.get('NewAccessToken', None)

class GetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetResultSet(response, path)
