# -*- coding: utf-8 -*-

###############################################################################
#
# Names
# Retrieves first and last names for the user and user's profiles.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Names(Choreography):

    """
    Create a new instance of the Names Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/23andMe/Names')


    def new_input_set(self):
        return NamesInputSet()

    def _make_result_set(self, result, path):
        return NamesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NamesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Names
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class NamesInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after completing the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the Names choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class NamesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from 23AndMe.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class NamesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NamesResultSet(response, path)
