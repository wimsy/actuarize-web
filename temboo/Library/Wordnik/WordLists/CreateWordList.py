# -*- coding: utf-8 -*-

###############################################################################
#
# CreateWordList
# Creates a new word list for the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateWordList(Choreography):

    """
    Create a new instance of the CreateWordList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/WordLists/CreateWordList')


    def new_input_set(self):
        return CreateWordListInputSet()

    def _make_result_set(self, result, path):
        return CreateWordListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateWordListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateWordList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateWordListInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from Wordnik.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ListDescription input for this choreography. ((required, string) A description of the list to create.)
        """
        def set_ListDescription(self, value):
            InputSet._set_input(self, 'ListDescription', value)

        """
        Set the value of the ListName input for this choreography. ((required, string) Name of list to create.)
        """
        def set_ListName(self, value):
            InputSet._set_input(self, 'ListName', value)

        """
        Set the value of the ListStatus input for this choreography. ((optional, string) Determines whether the list to cretae is public or private. Acceptable values: PUBLIC or PRIVATE.)
        """
        def set_ListStatus(self, value):
            InputSet._set_input(self, 'ListStatus', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The Password of the Wordnik account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The Username of the Wordnik account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateWordList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateWordListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Wordnik.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateWordListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateWordListResultSet(response, path)
