# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAllStatuses
# Shares a post across multiple social networks such as Facebook, Tumblr, and Twitter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateAllStatuses(Choreography):

    """
    Create a new instance of the UpdateAllStatuses Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/Social/UpdateAllStatuses')


    def new_input_set(self):
        return UpdateAllStatusesInputSet()

    def _make_result_set(self, result, path):
        return UpdateAllStatusesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAllStatusesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateAllStatuses
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateAllStatusesInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((required, string) A list of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Message input for this choreography. ((required, string) The message to be posted across social networks.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateAllStatuses choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateAllStatusesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) A list of results for each API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateAllStatusesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAllStatusesResultSet(response, path)
