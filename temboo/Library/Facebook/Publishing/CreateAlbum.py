# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAlbum
# Creates an album.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateAlbum(Choreography):

    """
    Create a new instance of the CreateAlbum Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/CreateAlbum')


    def new_input_set(self):
        return CreateAlbumInputSet()

    def _make_result_set(self, result, path):
        return CreateAlbumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAlbumChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateAlbum
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateAlbumInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Message input for this choreography. ((optional, string) A message to attach to the album.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Name input for this choreography. ((required, string) The name of the album.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ProfileID input for this choreography. ((optional, string) The id for the profile that the album will be published to. Defaults to "me" indicating the authenticated user.)
        """
        def set_ProfileID(self, value):
            InputSet._set_input(self, 'ProfileID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the CreateAlbum choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateAlbumResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateAlbumChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAlbumResultSet(response, path)
