# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveBlogFollowers
# Retrieves the count of followers for a specified Tumblr blog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveBlogFollowers(Choreography):

    """
    Create a new instance of the RetrieveBlogFollowers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/RetrieveBlogFollowers')


    def new_input_set(self):
        return RetrieveBlogFollowersInputSet()

    def _make_result_set(self, result, path):
        return RetrieveBlogFollowersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveBlogFollowersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveBlogFollowers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveBlogFollowersInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

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
        Set the value of the BaseHostname input for this choreography. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com))
        """
        def set_BaseHostname(self, value):
            InputSet._set_input(self, 'BaseHostname', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to return: 1 - 20. Defaults to 20.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The result to start at. Defaults to 0.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveBlogFollowers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveBlogFollowersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Tumblr in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveBlogFollowersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveBlogFollowersResultSet(response, path)
