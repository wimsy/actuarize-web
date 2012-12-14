# -*- coding: utf-8 -*-

###############################################################################
#
# GetAudio
# Retrieves the audio pronunciation of a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAudio(Choreography):

    """
    Create a new instance of the GetAudio Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Word/GetAudio')


    def new_input_set(self):
        return GetAudioInputSet()

    def _make_result_set(self, result, path):
        return GetAudioResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAudioChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAudio
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAudioInputSet(InputSet):
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
        Set the value of the Limit input for this choreography. ((optional, integer) Maximum number of results to return. Defaults to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

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
A ResultSet with methods tailored to the values returned by the GetAudio choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAudioResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAudioChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAudioResultSet(response, path)
