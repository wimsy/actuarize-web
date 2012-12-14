# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateProfile
# Update's a user's profile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateProfile(Choreography):

    """
    Create a new instance of the UpdateProfile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Profile/UpdateProfile')


    def new_input_set(self):
        return UpdateProfileInputSet()

    def _make_result_set(self, result, path):
        return UpdateProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateProfileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateProfile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateProfileInputSet(InputSet):
        """
        Set the value of the Profile input for this choreography. ((required, json) A JSON string containing the key/value pairs for the profile fields to update. See documentation for formatting examples.)
        """
        def set_Profile(self, value):
            InputSet._set_input(self, 'Profile', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateProfile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateProfileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from RunKeeper.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateProfileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateProfileResultSet(response, path)
