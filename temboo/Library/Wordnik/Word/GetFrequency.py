# -*- coding: utf-8 -*-

###############################################################################
#
# GetFrequency
# Retrieves the word frequency of a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetFrequency(Choreography):

    """
    Create a new instance of the GetFrequency Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Word/GetFrequency')


    def new_input_set(self):
        return GetFrequencyInputSet()

    def _make_result_set(self, result, path):
        return GetFrequencyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFrequencyChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetFrequency
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetFrequencyInputSet(InputSet):
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
        Set the value of the EndYear input for this choreography. ((optional, integer) End year for which to return word use frequencies. Defaults to 2012.)
        """
        def set_EndYear(self, value):
            InputSet._set_input(self, 'EndYear', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the StartYear input for this choreography. ((optional, integer) Start year for which to return word use frequencies. Defaults to 1800.)
        """
        def set_StartYear(self, value):
            InputSet._set_input(self, 'StartYear', value)

        """
        Set the value of the Word input for this choreography. ((required, string) The word you want to look up on Wordnik.)
        """
        def set_Word(self, value):
            InputSet._set_input(self, 'Word', value)


"""
A ResultSet with methods tailored to the values returned by the GetFrequency choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetFrequencyResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetFrequencyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFrequencyResultSet(response, path)
