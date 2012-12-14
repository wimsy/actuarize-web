# -*- coding: utf-8 -*-

###############################################################################
#
# StartServer
# Start a server associated with a particular Server ID.  Optionally, this Choreo can also poll the startup process and verify server startup.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class StartServer(Choreography):

    """
    Create a new instance of the StartServer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RightScale/StartServer')


    def new_input_set(self):
        return StartServerInputSet()

    def _make_result_set(self, result, path):
        return StartServerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StartServerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the StartServer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StartServerInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((required, string) The RightScale Account ID.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the Password input for this choreography. ((required, password) The RightScale account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PollingTimeLimit input for this choreography. ((optional, integer) Server status polling.  Enable by specifying a time limit - in minutes - for the duration of the server state polling.)
        """
        def set_PollingTimeLimit(self, value):
            InputSet._set_input(self, 'PollingTimeLimit', value)

        """
        Set the value of the ServerID input for this choreography. ((required, integer) The RightScale Server ID that is to be stopped.)
        """
        def set_ServerID(self, value):
            InputSet._set_input(self, 'ServerID', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The RightScale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the StartServer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StartServerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "State" output from this choreography execution. ((string) The server 'state' parsed from the Rightscale response.)
        """
        def get_State(self):
            return self._output.get('State', None)

class StartServerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StartServerResultSet(response, path)