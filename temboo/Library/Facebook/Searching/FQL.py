# -*- coding: utf-8 -*-

###############################################################################
#
# FQL
# Allows you to use a SQL-style syntax to query data in the Graph API.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FQL(Choreography):

    """
    Create a new instance of the FQL Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Searching/FQL')


    def new_input_set(self):
        return FQLInputSet()

    def _make_result_set(self, result, path):
        return FQLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FQLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FQL
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FQLInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Conditions input for this choreography. ((required, string) The conditions to use in the WHERE clause of the FQL statement.)
        """
        def set_Conditions(self, value):
            InputSet._set_input(self, 'Conditions', value)

        """
        Set the value of the Fields input for this choreography. ((required, string) The fields to return in the response.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Table input for this choreography. ((required, string) The table to select records from.)
        """
        def set_Table(self, value):
            InputSet._set_input(self, 'Table', value)


"""
A ResultSet with methods tailored to the values returned by the FQL choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FQLResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FQLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FQLResultSet(response, path)
