# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEntry
# Adds a diabetes measurement entry to a user's feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateEntry(Choreography):

    """
    Create a new instance of the CreateEntry Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/DiabetesMeasurements/CreateEntry')


    def new_input_set(self):
        return CreateEntryInputSet()

    def _make_result_set(self, result, path):
        return CreateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEntryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateEntry
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateEntryInputSet(InputSet):
        """
        Set the value of the Entry input for this choreography. ((required, json) A JSON string containing the key/value pairs for the diabetes measurement entry to create. See documentation for formatting examples.)
        """
        def set_Entry(self, value):
            InputSet._set_input(self, 'Entry', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the CreateEntry choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateEntryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) Contains the string 'true" when a new entry is created successfully.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "URI" output from this choreography execution. ((string) The entry uri that was created.)
        """
        def get_URI(self):
            return self._output.get('URI', None)

class CreateEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEntryResultSet(response, path)
