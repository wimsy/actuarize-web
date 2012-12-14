# -*- coding: utf-8 -*-

###############################################################################
#
# User
# Retrieves the user id, and a list of profiles including their ids and whether or not they are genotyped.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class User(Choreography):

    """
    Create a new instance of the User Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/23andMe/User')


    def new_input_set(self):
        return UserInputSet()

    def _make_result_set(self, result, path):
        return UserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the User
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UserInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after completing the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the User choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from 23AndMe.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserResultSet(response, path)
