# -*- coding: utf-8 -*-

###############################################################################
#
# GetExamples
# Retrieves the examples of a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetExamples(Choreography):

    """
    Create a new instance of the GetExamples Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Word/GetExamples')


    def new_input_set(self):
        return GetExamplesInputSet()

    def _make_result_set(self, result, path):
        return GetExamplesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetExamplesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetExamples
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetExamplesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Cannonical input for this choreography. ((optional, string) If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested. Defaults to false.)
        """
        def set_Cannonical(self, value):
            InputSet._set_input(self, 'Cannonical', value)

        """
        Set the value of the Duplicates input for this choreography. ((optional, string) Shows duplicate examples from different sources when set to true. Defaults to false.)
        """
        def set_Duplicates(self, value):
            InputSet._set_input(self, 'Duplicates', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Maximum number of results to return.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Skip input for this choreography. ((optional, integer) Results to skip. Defaults to 0.)
        """
        def set_Skip(self, value):
            InputSet._set_input(self, 'Skip', value)

        """
        Set the value of the Word input for this choreography. ((required, string) The word you want to look up on Wordnik.)
        """
        def set_Word(self, value):
            InputSet._set_input(self, 'Word', value)


"""
A ResultSet with methods tailored to the values returned by the GetExamples choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetExamplesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetExamplesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetExamplesResultSet(response, path)
