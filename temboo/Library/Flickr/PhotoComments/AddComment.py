# -*- coding: utf-8 -*-

###############################################################################
#
# AddComment
# Add a comment to a specified photo on Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddComment(Choreography):

    """
    Create a new instance of the AddComment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/PhotoComments/AddComment')


    def new_input_set(self):
        return AddCommentInputSet()

    def _make_result_set(self, result, path):
        return AddCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCommentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddComment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddCommentInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CommentText input for this choreography. ((required, string) The text of the comment you are adding.)
        """
        def set_CommentText(self, value):
            InputSet._set_input(self, 'CommentText', value)

        """
        Set the value of the PhotoId input for this choreography. ((required, integer) The id of the photo to add a comment to)
        """
        def set_PhotoId(self, value):
            InputSet._set_input(self, 'PhotoId', value)


"""
A ResultSet with methods tailored to the values returned by the AddComment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddCommentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddCommentResultSet(response, path)
