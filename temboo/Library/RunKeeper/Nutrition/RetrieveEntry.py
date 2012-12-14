# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveEntry
# Retrieves a nutrition entry from a user’s feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveEntry(Choreography):

    """
    Create a new instance of the RetrieveEntry Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Nutrition/RetrieveEntry')


    def new_input_set(self):
        return RetrieveEntryInputSet()

    def _make_result_set(self, result, path):
        return RetrieveEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveEntryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveEntry
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveEntryInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the EntryID input for this choreography. ((required, string) This can be the individual id of the nutrition entry, or you can pass the full uri for the entry as returned from the RetrieveEntries Choreo (i.e. /nutrition/-12985593-1350950400000).)
        """
        def set_EntryID(self, value):
            InputSet._set_input(self, 'EntryID', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveEntry choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveEntryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from RunKeeper.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveEntryResultSet(response, path)
