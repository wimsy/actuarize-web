# -*- coding: utf-8 -*-

###############################################################################
#
# UploadPhoto
# Uploads a photo to a given album.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadPhoto(Choreography):

    """
    Create a new instance of the UploadPhoto Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/UploadPhoto')


    def new_input_set(self):
        return UploadPhotoInputSet()

    def _make_result_set(self, result, path):
        return UploadPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadPhotoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadPhoto
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadPhotoInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the AlbumID input for this choreography. ((required, string) The id of the album to upload the photo to.)
        """
        def set_AlbumID(self, value):
            InputSet._set_input(self, 'AlbumID', value)

        """
        Set the value of the Message input for this choreography. ((optional, string) A message to attach to the photo.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Photo input for this choreography. ((conditional, any) The image contents formatted as a Base64 encoded string.)
        """
        def set_Photo(self, value):
            InputSet._set_input(self, 'Photo', value)

        """
        Set the value of the Place input for this choreography. ((optional, string) A location associated with a Photo.)
        """
        def set_Place(self, value):
            InputSet._set_input(self, 'Place', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Source input for this choreography. ((optional, string) A link to the source image of the photo.)
        """
        def set_Source(self, value):
            InputSet._set_input(self, 'Source', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to image in the vault. This can be used as an alternative to the Photo input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadPhoto choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadPhotoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadPhotoResultSet(response, path)
