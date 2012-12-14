# -*- coding: utf-8 -*-

###############################################################################
#
# ByKloutID
# Performs a lookup for a user's identity using a Klout ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByKloutID(Choreography):

    """
    Create a new instance of the ByKloutID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Klout/Identity/ByKloutID')


    def new_input_set(self):
        return ByKloutIDInputSet()

    def _make_result_set(self, result, path):
        return ByKloutIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByKloutIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByKloutID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByKloutIDInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Klout.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the KloutID input for this choreography. ((required, integer) The numeric ID for a Klout user.)
        """
        def set_KloutID(self, value):
            InputSet._set_input(self, 'KloutID', value)


"""
A ResultSet with methods tailored to the values returned by the ByKloutID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByKloutIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Klout.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByKloutIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByKloutIDResultSet(response, path)
