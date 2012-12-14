# -*- coding: utf-8 -*-

###############################################################################
#
# GetContacts
# Retrieves your social contacts from multiple APIs in one API call.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetContacts(Choreography):

    """
    Create a new instance of the GetContacts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/Social/GetContacts')


    def new_input_set(self):
        return GetContactsInputSet()

    def _make_result_set(self, result, path):
        return GetContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContactsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetContacts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetContactsInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((conditional, json) A list of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the ScreenName input for this choreography. ((conditional, string) The Twitter screen name to retrieve followers for.)
        """
        def set_ScreenName(self, value):
            InputSet._set_input(self, 'ScreenName', value)


"""
A ResultSet with methods tailored to the values returned by the GetContacts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetContactsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) Contains the merged results from the API responses.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetContactsResultSet(response, path)
