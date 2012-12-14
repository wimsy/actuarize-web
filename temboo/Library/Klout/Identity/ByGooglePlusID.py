# -*- coding: utf-8 -*-

###############################################################################
#
# ByGooglePlusID
# Performs a lookup for a user's identity using a Google+ ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByGooglePlusID(Choreography):

    """
    Create a new instance of the ByGooglePlusID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Klout/Identity/ByGooglePlusID')


    def new_input_set(self):
        return ByGooglePlusIDInputSet()

    def _make_result_set(self, result, path):
        return ByGooglePlusIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByGooglePlusIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByGooglePlusID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByGooglePlusIDInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Klout.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the GooglePlusID input for this choreography. ((required, integer) The numeric ID for a Google+ user.)
        """
        def set_GooglePlusID(self, value):
            InputSet._set_input(self, 'GooglePlusID', value)


"""
A ResultSet with methods tailored to the values returned by the ByGooglePlusID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByGooglePlusIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Klout.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByGooglePlusIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByGooglePlusIDResultSet(response, path)
