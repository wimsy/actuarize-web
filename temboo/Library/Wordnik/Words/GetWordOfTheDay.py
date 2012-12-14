# -*- coding: utf-8 -*-

###############################################################################
#
# GetWordOfTheDay
# Retrieves the word of the day for specified dates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWordOfTheDay(Choreography):

    """
    Create a new instance of the GetWordOfTheDay Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Words/GetWordOfTheDay')


    def new_input_set(self):
        return GetWordOfTheDayInputSet()

    def _make_result_set(self, result, path):
        return GetWordOfTheDayResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWordOfTheDayChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWordOfTheDay
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWordOfTheDayInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Date input for this choreography. ((required, string) The date of the Word of the Day to retrieve, in yyyy-MM-dd format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetWordOfTheDay choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWordOfTheDayResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWordOfTheDayChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWordOfTheDayResultSet(response, path)
