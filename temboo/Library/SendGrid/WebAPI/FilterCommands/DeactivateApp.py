# -*- coding: utf-8 -*-

###############################################################################
#
# DeactivateApp
# Deactivate an app.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeactivateApp(Choreography):

    """
    Create a new instance of the DeactivateApp Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/FilterCommands/DeactivateApp')


    def new_input_set(self):
        return DeactivateAppInputSet()

    def _make_result_set(self, result, path):
        return DeactivateAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeactivateAppChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeactivateApp
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeactivateAppInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from SendGrid.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIUser input for this choreography. ((required, string) The username registered with SendGrid.)
        """
        def set_APIUser(self, value):
            InputSet._set_input(self, 'APIUser', value)

        """
        Set the value of the AppName input for this choreography. ((required, string) The name of the app to be activated.  A list of available apps can be obtained by running the ListAvailableApps Choreo.)
        """
        def set_AppName(self, value):
            InputSet._set_input(self, 'AppName', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the DeactivateApp choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeactivateAppResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeactivateAppChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeactivateAppResultSet(response, path)
