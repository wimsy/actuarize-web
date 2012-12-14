# -*- coding: utf-8 -*-

###############################################################################
#
# GetWordList
# Retrieves a word list by its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWordList(Choreography):

    """
    Create a new instance of the GetWordList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/WordList/GetWordList')


    def new_input_set(self):
        return GetWordListInputSet()

    def _make_result_set(self, result, path):
        return GetWordListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWordListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWordList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWordListInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The Password of the Wordnik account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The Username of the Wordnik account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WordList input for this choreography. ((required, string) The perma-link for the Word List to retrieve.)
        """
        def set_WordList(self, value):
            InputSet._set_input(self, 'WordList', value)


"""
A ResultSet with methods tailored to the values returned by the GetWordList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWordListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWordListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWordListResultSet(response, path)
