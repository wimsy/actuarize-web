# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecordsById
# Retrieves records from your Zoho CRM account by ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecordsById(Choreography):

    """
    Create a new instance of the GetRecordsById Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GetRecordsById')


    def new_input_set(self):
        return GetRecordsByIdInputSet()

    def _make_result_set(self, result, path):
        return GetRecordsByIdResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecordsByIdChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecordsById
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecordsByIdInputSet(InputSet):
        """
        Set the value of the AuthenticationToken input for this choreography. ((required, string) A valid authentication token. Permanent authentication tokens can be generated by the GenerateAuthToken Choreo.)
        """
        def set_AuthenticationToken(self, value):
            InputSet._set_input(self, 'AuthenticationToken', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The ID for the Zoho record to lookup)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the Module input for this choreography. ((optional, string) The Zoho module you want to access. Defaults to 'Leads'.)
        """
        def set_Module(self, value):
            InputSet._set_input(self, 'Module', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid formats are: json and xml (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecordsById choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecordsByIdResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Zoho. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecordsByIdChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecordsByIdResultSet(response, path)
