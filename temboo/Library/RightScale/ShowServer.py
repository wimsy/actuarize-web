# -*- coding: utf-8 -*-

###############################################################################
#
# ShowServer
# Display a comrephensive set of information about the querried server such as: state information, server templates used, SSH key href, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ShowServer(Choreography):

    """
    Create a new instance of the ShowServer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RightScale/ShowServer')


    def new_input_set(self):
        return ShowServerInputSet()

    def _make_result_set(self, result, path):
        return ShowServerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowServerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ShowServer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShowServerInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the ShowServer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShowServerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShowServerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowServerResultSet(response, path)
