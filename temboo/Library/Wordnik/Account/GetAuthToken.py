# -*- coding: utf-8 -*-

###############################################################################
#
# GetAuthToken
# Obtains an authentication token for use in other Wordnik Choreos.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAuthToken(Choreography):

    """
    Create a new instance of the GetAuthToken Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Account/GetAuthToken')


    def new_input_set(self):
        return GetAuthTokenInputSet()

    def _make_result_set(self, result, path):
        return GetAuthTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAuthTokenChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAuthToken
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAuthTokenInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Password of the Wordnik account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Username of the Wordnik account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetAuthToken choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAuthTokenResultSet(ResultSet):
        """
        Retrieve the value for the "Token" output from this choreography execution. (The Token obtained from running this Choreo.)
        """
        def get_Token(self):
            return self._output.get('Token', None)

class GetAuthTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAuthTokenResultSet(response, path)
