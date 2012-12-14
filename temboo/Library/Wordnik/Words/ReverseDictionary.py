# -*- coding: utf-8 -*-

###############################################################################
#
# ReverseDictionary
# Retrieves a reverse dictionary search for a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ReverseDictionary(Choreography):

    """
    Create a new instance of the ReverseDictionary Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Words/ReverseDictionary')


    def new_input_set(self):
        return ReverseDictionaryInputSet()

    def _make_result_set(self, result, path):
        return ReverseDictionaryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReverseDictionaryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ReverseDictionary
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ReverseDictionaryInputSet(InputSet):
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
        Set the value of the ExcludeSource input for this choreography. ((optional, string) Exclude these comma-delimited source dictionaries: ahd, century, wiktionary,webster, wordnet.)
        """
        def set_ExcludeSource(self, value):
            InputSet._set_input(self, 'ExcludeSource', value)

        """
        Set the value of the ExpandTerms input for this choreography. ((optional, any) Expand terms by either: synonym or hypernym.)
        """
        def set_ExpandTerms(self, value):
            InputSet._set_input(self, 'ExpandTerms', value)

        """
        Set the value of the IncludePartOfSpeech input for this choreography. ((optional, string) Only includes the specified comma-delimited parts of speech. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        def set_IncludePartOfSpeech(self, value):
            InputSet._set_input(self, 'IncludePartOfSpeech', value)

        """
        Set the value of the IncludeSource input for this choreography. ((optional, string) Only include these comma-delimited source dictionaries: ahd, century, wiktionary,webster, wordnet.)
        """
        def set_IncludeSource(self, value):
            InputSet._set_input(self, 'IncludeSource', value)

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
        Set the value of the MinLength input for this choreography. ((optional, integer) ‪Minimum word length.)
        """
        def set_MinLength(self, value):
            InputSet._set_input(self, 'MinLength', value)

        """
        Set the value of the Query input for this choreography. ((required, string) Word or fragment to query for in Wordnik.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Skip input for this choreography. ((optional, integer) Number of results to skip.)
        """
        def set_Skip(self, value):
            InputSet._set_input(self, 'Skip', value)

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
        Set the value of the WordSense input for this choreography. ((optional, string) Restricts words and finds the closest sense to the one indicated.)
        """
        def set_WordSense(self, value):
            InputSet._set_input(self, 'WordSense', value)


"""
A ResultSet with methods tailored to the values returned by the ReverseDictionary choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ReverseDictionaryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ReverseDictionaryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReverseDictionaryResultSet(response, path)
