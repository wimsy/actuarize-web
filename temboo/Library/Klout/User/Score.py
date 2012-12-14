# -*- coding: utf-8 -*-

###############################################################################
#
# Score
# Retrieves a user's Klout Score and deltas.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Score(Choreography):

    """
    Create a new instance of the Score Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Klout/User/Score')


    def new_input_set(self):
        return ScoreInputSet()

    def _make_result_set(self, result, path):
        return ScoreResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ScoreChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Score
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ScoreInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Klout.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the KloutID input for this choreography. ((required, string) The id for a Klout user to retrieve a score for.)
        """
        def set_KloutID(self, value):
            InputSet._set_input(self, 'KloutID', value)


"""
A ResultSet with methods tailored to the values returned by the Score choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ScoreResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Klout.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ScoreChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ScoreResultSet(response, path)
