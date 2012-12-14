# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveRecords
# Returns the feed for a user's personal records.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveRecords(Choreography):

    """
    Create a new instance of the RetrieveRecords Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/PersonalRecords/RetrieveRecords')


    def new_input_set(self):
        return RetrieveRecordsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveRecordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveRecordsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveRecords
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveRecordsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveRecords choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveRecordsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from RunKeeper.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveRecordsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveRecordsResultSet(response, path)
