# -*- coding: utf-8 -*-

###############################################################################
#
# GetRelatedWords
# Retrieves the related words of a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRelatedWords(Choreography):

    """
    Create a new instance of the GetRelatedWords Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Word/GetRelatedWords')


    def new_input_set(self):
        return GetRelatedWordsInputSet()

    def _make_result_set(self, result, path):
        return GetRelatedWordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRelatedWordsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRelatedWords
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRelatedWordsInputSet(InputSet):
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
        Set the value of the LimitPerType input for this choreography. ((optional, integer) Limits the amount of results returned for each relationship type included in the output. Defaults to 10.)
        """
        def set_LimitPerType(self, value):
            InputSet._set_input(self, 'LimitPerType', value)

        """
        Set the value of the RelationshipType input for this choreography. ((optional, string) Limits the total results per type of relationship. Acceptable values inlcude adjective, noun, etc. See docs for complete list.)
        """
        def set_RelationshipType(self, value):
            InputSet._set_input(self, 'RelationshipType', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Word input for this choreography. ((required, string) The word you want to look up on Wordnik.)
        """
        def set_Word(self, value):
            InputSet._set_input(self, 'Word', value)


"""
A ResultSet with methods tailored to the values returned by the GetRelatedWords choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRelatedWordsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRelatedWordsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRelatedWordsResultSet(response, path)
