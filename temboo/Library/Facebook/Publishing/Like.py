# -*- coding: utf-8 -*-

###############################################################################
#
# Like
# Allows a user to "like" a Graph API object.
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
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/Like')


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
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ObjectID input for this choreography. ((required, string) The id of a graph api object to like.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)


"""
A ResultSet with methods tailored to the values returned by the Like choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LikeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LikeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikeResultSet(response, path)
