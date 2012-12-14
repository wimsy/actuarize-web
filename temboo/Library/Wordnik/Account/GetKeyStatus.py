# -*- coding: utf-8 -*-

###############################################################################
#
# GetKeyStatus
# Obtains the status of the user's current API Key.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetKeyStatus(Choreography):

    """
    Create a new instance of the GetKeyStatus Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Account/GetKeyStatus')


    def new_input_set(self):
        return GetKeyStatusInputSet()

    def _make_result_set(self, result, path):
        return GetKeyStatusResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetKeyStatusChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetKeyStatus
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetKeyStatusInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetKeyStatus choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetKeyStatusResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetKeyStatusChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetKeyStatusResultSet(response, path)
