# -*- coding: utf-8 -*-

###############################################################################
#
# GetListEmailAddresses
# Retrieve email addresses associated with a specified Recipient List.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetListEmailAddresses(Choreography):

    """
    Create a new instance of the GetListEmailAddresses Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/ListsEmail/GetListEmailAddresses')


    def new_input_set(self):
        return GetListEmailAddressesInputSet()

    def _make_result_set(self, result, path):
        return GetListEmailAddressesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListEmailAddressesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetListEmailAddresses
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListEmailAddressesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from SendGrid.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIUser input for this choreography. ((required, string) The username registered with SendGrid.)
        """
        def set_APIUser(self, value):
            InputSet._set_input(self, 'APIUser', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) The email address to search for in a recipient list.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the List input for this choreography. ((required, string) The recipient list from which email addresses will be retrieved.  Must be an existing recipient list.)
        """
        def set_List(self, value):
            InputSet._set_input(self, 'List', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the GetListEmailAddresses choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListEmailAddressesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListEmailAddressesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListEmailAddressesResultSet(response, path)
