# -*- coding: utf-8 -*-

###############################################################################
#
# AddPost
# Posts user-generated content from an external app to a Foursquare check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddPost(Choreography):

    """
    Create a new instance of the AddPost Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/AddPost')


    def new_input_set(self):
        return AddPostInputSet()

    def _make_result_set(self, result, path):
        return AddPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddPostChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddPost
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddPostInputSet(InputSet):
        """
        Set the value of the CheckinID input for this choreography. ((required, string) The ID of the check-in to add a post to.)
        """
        def set_CheckinID(self, value):
            InputSet._set_input(self, 'CheckinID', value)

        """
        Set the value of the ContentID input for this choreography. ((optional, string) An ID for the post to be used in a native link. Can be up to 50 characters. The URL input must also be specified when using this parameter.)
        """
        def set_ContentID(self, value):
            InputSet._set_input(self, 'ContentID', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Text input for this choreography. ((required, string) The text of the post. Max length is 200 characters.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)

        """
        Set the value of the URL input for this choreography. ((optional, string) A URL linking to more details. The following URL schemes are supported: http, https, foursquare, mailto, tel, and sms.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the AddPost choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddPostResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddPostResultSet(response, path)
