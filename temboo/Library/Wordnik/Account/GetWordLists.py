# -*- coding: utf-8 -*-

###############################################################################
#
# GetWordLists
# Retrieves the word lists for the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWordLists(Choreography):

    """
    Create a new instance of the GetWordLists Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Account/GetWordLists')


    def new_input_set(self):
        return GetWordListsInputSet()

    def _make_result_set(self, result, path):
        return GetWordListsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWordListsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWordLists
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWordListsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Maximum number of results to return. Defaults to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

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
        Set the value of the Skip input for this choreography. ((optional, integer) Number of results to skip. Defaults to 0.)
        """
        def set_Skip(self, value):
            InputSet._set_input(self, 'Skip', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The Username of the Wordnik account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetWordLists choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWordListsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWordListsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWordListsResultSet(response, path)
