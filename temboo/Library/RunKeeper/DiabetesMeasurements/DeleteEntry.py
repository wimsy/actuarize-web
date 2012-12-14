# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteEntry
# Removes an individual diabetes measurement entry from a user’s feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteEntry(Choreography):

    """
    Create a new instance of the DeleteEntry Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/DiabetesMeasurements/DeleteEntry')


    def new_input_set(self):
        return DeleteEntryInputSet()

    def _make_result_set(self, result, path):
        return DeleteEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteEntryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteEntry
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteEntryInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the EntryID input for this choreography. ((required, string) This can be the individual id of the diabetes measurement entry, or you can pass the full uri for the entry as returned from the RetrieveEntries Choreo (i.e. /diabetes/12985593).)
        """
        def set_EntryID(self, value):
            InputSet._set_input(self, 'EntryID', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteEntry choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteEntryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) Contains the string "true" when an entry is deleted successfully.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteEntryResultSet(response, path)
