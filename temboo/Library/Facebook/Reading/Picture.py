# -*- coding: utf-8 -*-

###############################################################################
#
# Picture
# Retrieves the current profile photo for any object in the Facebook graph, and returns the image as a Base64 encoded string.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Picture(Choreography):

    """
    Create a new instance of the Picture Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/Picture')


    def new_input_set(self):
        return PictureInputSet()

    def _make_result_set(self, result, path):
        return PictureResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PictureChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Picture
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PictureInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ProfileID input for this choreography. ((required, string) The id of the profile to retrieve a profile picture for. Defaults to "me" indicating the authenticated user.)
        """
        def set_ProfileID(self, value):
            InputSet._set_input(self, 'ProfileID', value)

        """
        Set the value of the ReturnSSLResources input for this choreography. ((optional, boolean) Set to 1 to return the picture over a secure connection. Defaults to 0.)
        """
        def set_ReturnSSLResources(self, value):
            InputSet._set_input(self, 'ReturnSSLResources', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The size of the image to retrieve. Valid values: square (50x50), small (50 pixels wide, variable height), normal (100 pixels wide, variable height), and large (about 200 pixels wide, variable height))
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the Picture choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PictureResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Contains the Base64 encoded value of the image retrieved from Facebook.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PictureChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PictureResultSet(response, path)
