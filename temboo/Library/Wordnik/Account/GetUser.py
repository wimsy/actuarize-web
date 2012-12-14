# -*- coding: utf-8 -*-

###############################################################################
#
# GetUser
# Retrieves information on the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetUser(Choreography):

    """
    Create a new instance of the GetUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Account/GetUser')


    def new_input_set(self):
        return GetUserInputSet()

    def _make_result_set(self, result, path):
        return GetUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetUserInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Password of the Wordnik account. )
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Username of the Wordnik account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUserResultSet(response, path)
