# -*- coding: utf-8 -*-

###############################################################################
#
# Like
# Allows the authenticated user to like or unlike a check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Like(Choreography):

    """
    Create a new instance of the Like Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/Like')


    def new_input_set(self):
        return LikeInputSet()

    def _make_result_set(self, result, path):
        return LikeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Like
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LikeInputSet(InputSet):
        """
        Set the value of the CheckinID input for this choreography. ((required, string) The ID of the check-in to like or unlike.)
        """
        def set_CheckinID(self, value):
            InputSet._set_input(self, 'CheckinID', value)

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
        Set the value of the Set input for this choreography. ((optional, boolean) Set to 1 (the default) to like this check-in. Set to 0 to undo a previous like.)
        """
        def set_Set(self, value):
            InputSet._set_input(self, 'Set', value)


"""
A ResultSet with methods tailored to the values returned by the Like choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LikeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LikeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikeResultSet(response, path)
