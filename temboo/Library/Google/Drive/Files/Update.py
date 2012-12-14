# -*- coding: utf-8 -*-

###############################################################################
#
# Update
# Updates the metadata or content of an existing file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Update(Choreography):

    """
    Create a new instance of the Update Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Files/Update')


    def new_input_set(self):
        return UpdateInputSet()

    def _make_result_set(self, result, path):
        return UpdateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Update
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateInputSet(InputSet):
        """
        Set the value of the RequestBody input for this choreography. ((conditional, json) A JSON representation of fields in a file resource. File metadata information (such as the title) can be updated using this input. See documentation for formatting examples.)
        """
        def set_RequestBody(self, value):
            InputSet._set_input(self, 'RequestBody', value)

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
        Set the value of the ContentType input for this choreography. ((conditional, string) The Content-Type of the file that is being updated (i.e. image/jpeg). Required if modifying the file content.)
        """
        def set_ContentType(self, value):
            InputSet._set_input(self, 'ContentType', value)

        """
        Set the value of the Convert input for this choreography. ((optional, boolean) Whether to convert this file to the corresponding Google Docs format. (Default: false).)
        """
        def set_Convert(self, value):
            InputSet._set_input(self, 'Convert', value)

        """
        Set the value of the Fields input for this choreography. ((optional, string) Selector specifying which fields to include in a partial response.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the FileContent input for this choreography. ((conditional, string) The new Base64 encoded contents of the file that is being updated.)
        """
        def set_FileContent(self, value):
            InputSet._set_input(self, 'FileContent', value)

        """
        Set the value of the FileID input for this choreography. ((required, string) The id of the file to update.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)

        """
        Set the value of the OCR input for this choreography. ((optional, boolean) Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. (Default: false))
        """
        def set_OCR(self, value):
            InputSet._set_input(self, 'OCR', value)

        """
        Set the value of the OcrLanguage input for this choreography. ((optional, string) If ocr is true, hints at the language to use. Valid values are ISO 639-1 codes.)
        """
        def set_OcrLanguage(self, value):
            InputSet._set_input(self, 'OcrLanguage', value)

        """
        Set the value of the Pinned input for this choreography. ((optional, boolean) Whether to pin the new revision. (Default: false).)
        """
        def set_Pinned(self, value):
            InputSet._set_input(self, 'Pinned', value)

        """
        Set the value of the RefreshToken input for this choreography. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the SetModifiedDate input for this choreography. ((optional, boolean) Whether to set the modified date with the supplied modified date.)
        """
        def set_SetModifiedDate(self, value):
            InputSet._set_input(self, 'SetModifiedDate', value)

        """
        Set the value of the SourceLanguage input for this choreography. ((optional, string) The language of the original file to be translated.)
        """
        def set_SourceLanguage(self, value):
            InputSet._set_input(self, 'SourceLanguage', value)

        """
        Set the value of the TargetLanguage input for this choreography. ((optional, string) Target language to translate the file to. If no sourceLanguage is provided, the API will attempt to detect the language.)
        """
        def set_TargetLanguage(self, value):
            InputSet._set_input(self, 'TargetLanguage', value)

        """
        Set the value of the TimedTextLanguage input for this choreography. ((optional, string) The language of the timed text.)
        """
        def set_TimedTextLanguage(self, value):
            InputSet._set_input(self, 'TimedTextLanguage', value)

        """
        Set the value of the TimedTextTrackName input for this choreography. ((optional, string) The timed text track name.)
        """
        def set_TimedTextTrackName(self, value):
            InputSet._set_input(self, 'TimedTextTrackName', value)

        """
        Set the value of the UpdateViewedDate input for this choreography. ((optional, boolean) Whether to update the view date after successfully updating the file.)
        """
        def set_UpdateViewedDate(self, value):
            InputSet._set_input(self, 'UpdateViewedDate', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to a vault file to upload. This can be used as an alternative to the FileContent input.)
        """


"""
A ResultSet with methods tailored to the values returned by the Update choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateResultSet(ResultSet):
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

class UpdateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateResultSet(response, path)
