# -*- coding: utf-8 -*-

###############################################################################
#
# Topics
# Retrieves a user's topics. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Topics(Choreography):

    """
    Create a new instance of the Topics Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Klout/User/Topics')


    def new_input_set(self):
        return TopicsInputSet()

    def _make_result_set(self, result, path):
        return TopicsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopicsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Topics
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TopicsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Klout.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the KloutID input for this choreography. ((required, string) The id for a Klout user to retrieve topics for.)
        """
        def set_KloutID(self, value):
            InputSet._set_input(self, 'KloutID', value)


"""
A ResultSet with methods tailored to the values returned by the Topics choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TopicsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Klout.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TopicsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopicsResultSet(response, path)
