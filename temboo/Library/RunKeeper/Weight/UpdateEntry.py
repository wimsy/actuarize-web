# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateEntry
# Updates a weight entry in a user’s feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateEntry(Choreography):

    """
    Create a new instance of the UpdateEntry Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Weight/UpdateEntry')


    def new_input_set(self):
        return UpdateEntryInputSet()

    def _make_result_set(self, result, path):
        return UpdateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateEntryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateEntry
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateEntryInputSet(InputSet):
        """
        Set the value of the Entry input for this choreography. ((required, json) A JSON string containing the key/value pairs for the fields to be updated in the weight entry. See documentation for formatting examples.)
        """
        def set_Entry(self, value):
            InputSet._set_input(self, 'Entry', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the EntryID input for this choreography. ((required, string) This can be the individual id of the weight entry, or you can pass the full uri for the entry as returned from the RetrieveEntries Choreo (i.e. /weight/24085455).)
        """
        def set_EntryID(self, value):
            InputSet._set_input(self, 'EntryID', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateEntry choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateEntryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from RunKeeper.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateEntryResultSet(response, path)
