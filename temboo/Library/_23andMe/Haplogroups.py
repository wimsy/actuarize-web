# -*- coding: utf-8 -*-

###############################################################################
#
# Haplogroups
# Retrieves maternal and paternal haplogroups for a user's profiles.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Haplogroups(Choreography):

    """
    Create a new instance of the Haplogroups Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/23andMe/Haplogroups')


    def new_input_set(self):
        return HaplogroupsInputSet()

    def _make_result_set(self, result, path):
        return HaplogroupsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HaplogroupsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Haplogroups
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class HaplogroupsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after completing the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the Haplogroups choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class HaplogroupsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from 23AndMe.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class HaplogroupsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HaplogroupsResultSet(response, path)
