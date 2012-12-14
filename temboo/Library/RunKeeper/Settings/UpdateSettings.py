# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateSettings
# Updates a user’s settings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateSettings(Choreography):

    """
    Create a new instance of the UpdateSettings Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Settings/UpdateSettings')


    def new_input_set(self):
        return UpdateSettingsInputSet()

    def _make_result_set(self, result, path):
        return UpdateSettingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateSettingsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateSettings
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateSettingsInputSet(InputSet):
        """
        Set the value of the Settings input for this choreography. ((required, json) A JSON string containing the key/value pairs for the settings to update. See documentation for formatting examples.)
        """
        def set_Settings(self, value):
            InputSet._set_input(self, 'Settings', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateSettings choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateSettingsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from RunKeeper.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateSettingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateSettingsResultSet(response, path)
