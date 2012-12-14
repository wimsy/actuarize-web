# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyProfileByName
# Retrieve a company profile by entering a company's universal-name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCompanyProfileByName(Choreography):

    """
    Create a new instance of the GetCompanyProfileByName Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Companies/GetCompanyProfileByName')


    def new_input_set(self):
        return GetCompanyProfileByNameInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyProfileByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyProfileByNameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCompanyProfileByName
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCompanyProfileByNameInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the CompanyName input for this choreography. ((required, integer) The unique string identifier for a company.)
        """
        def set_CompanyName(self, value):
            InputSet._set_input(self, 'CompanyName', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetCompanyProfileByName choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCompanyProfileByNameResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCompanyProfileByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyProfileByNameResultSet(response, path)
