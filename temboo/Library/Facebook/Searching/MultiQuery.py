# -*- coding: utf-8 -*-

###############################################################################
#
# MultiQuery
# Allows you to submit multiple FQL statements and retrieve all the results you need in one request.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MultiQuery(Choreography):

    """
    Create a new instance of the MultiQuery Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Searching/MultiQuery')


    def new_input_set(self):
        return MultiQueryInputSet()

    def _make_result_set(self, result, path):
        return MultiQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MultiQueryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MultiQuery
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MultiQueryInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Queries input for this choreography. ((required, json) A JSON dictionary containing multiple queries to execute. See documentation for formatting examples.)
        """
        def set_Queries(self, value):
            InputSet._set_input(self, 'Queries', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the MultiQuery choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MultiQueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MultiQueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MultiQueryResultSet(response, path)
