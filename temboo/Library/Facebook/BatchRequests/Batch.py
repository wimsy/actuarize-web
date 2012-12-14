# -*- coding: utf-8 -*-

###############################################################################
#
# Batch
# Allows you to perform multiple graph operations in one request.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Batch(Choreography):

    """
    Create a new instance of the Batch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/BatchRequests/Batch')


    def new_input_set(self):
        return BatchInputSet()

    def _make_result_set(self, result, path):
        return BatchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BatchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Batch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class BatchInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Batch input for this choreography. ((required, json) A JSON object which describes each individual operation you'd like to perform. See documentation for syntax examples.)
        """
        def set_Batch(self, value):
            InputSet._set_input(self, 'Batch', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Batch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class BatchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Contains the Base64 encoded value of the image retrieved from Facebook.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class BatchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BatchResultSet(response, path)
