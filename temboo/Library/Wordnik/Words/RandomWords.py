# -*- coding: utf-8 -*-

###############################################################################
#
# RandomWords
# Retrieves a list of random words.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RandomWords(Choreography):

    """
    Create a new instance of the RandomWords Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Words/RandomWords')


    def new_input_set(self):
        return RandomWordsInputSet()

    def _make_result_set(self, result, path):
        return RandomWordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RandomWordsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RandomWords
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RandomWordsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ExcludePartOfSpeech input for this choreography. ((optional, string) Excludes the specified comma-delimited parts of speech from the results returned. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        def set_ExcludePartOfSpeech(self, value):
            InputSet._set_input(self, 'ExcludePartOfSpeech', value)

        """
        Set the value of the HasDefinition input for this choreography. ((optional, string) Only returns words that have dictionary definitions when true. Otherwise false. Defaults to true.)
        """
        def set_HasDefinition(self, value):
            InputSet._set_input(self, 'HasDefinition', value)

        """
        Set the value of the IncludePartOfSpeech input for this choreography. ((optional, string) Only includes the specified comma-delimited parts of speech. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        def set_IncludePartOfSpeech(self, value):
            InputSet._set_input(self, 'IncludePartOfSpeech', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Maximum number of results to return. Defaults to 10.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the MaxCorpus input for this choreography. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count below the given number.)
        """
        def set_MaxCorpus(self, value):
            InputSet._set_input(self, 'MaxCorpus', value)

        """
        Set the value of the MaxDictionaries input for this choreography. ((optional, integer) Maximum number of dictionaries in which the words appear.)
        """
        def set_MaxDictionaries(self, value):
            InputSet._set_input(self, 'MaxDictionaries', value)

        """
        Set the value of the MaxLength input for this choreography. ((optional, integer) Maximum word length.)
        """
        def set_MaxLength(self, value):
            InputSet._set_input(self, 'MaxLength', value)

        """
        Set the value of the MinCorpus input for this choreography. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count above the given number.)
        """
        def set_MinCorpus(self, value):
            InputSet._set_input(self, 'MinCorpus', value)

        """
        Set the value of the MinDictionaries input for this choreography. ((optional, integer) Minimum number of dictionaries in which the words appear.)
        """
        def set_MinDictionaries(self, value):
            InputSet._set_input(self, 'MinDictionaries', value)

        """
        Set the value of the MinLength input for this choreography. ((optional, integer) ‪Minimum word length.)
        """
        def set_MinLength(self, value):
            InputSet._set_input(self, 'MinLength', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the SortBy input for this choreography. ((optional, string) Results can be sorted by: alpha, count, or length.)
        """
        def set_SortBy(self, value):
            InputSet._set_input(self, 'SortBy', value)

        """
        Set the value of the SortOrder input for this choreography. ((optional, string) Indicate the order to sort, either asc (ascending) or desc (descending).)
        """
        def set_SortOrder(self, value):
            InputSet._set_input(self, 'SortOrder', value)


"""
A ResultSet with methods tailored to the values returned by the RandomWords choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RandomWordsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RandomWordsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RandomWordsResultSet(response, path)
