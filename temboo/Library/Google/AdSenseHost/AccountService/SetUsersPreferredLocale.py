# -*- coding: utf-8 -*-

###############################################################################
#
# SetUsersPreferredLocale
# Set the user's preferred locale (language). All correspondence with the user will occur in this locale.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SetUsersPreferredLocale(Choreography):

    """
    Create a new instance of the SetUsersPreferredLocale Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/SetUsersPreferredLocale')


    def new_input_set(self):
        return SetUsersPreferredLocaleInputSet()

    def _make_result_set(self, result, path):
        return SetUsersPreferredLocaleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetUsersPreferredLocaleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SetUsersPreferredLocale
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SetUsersPreferredLocaleInputSet(InputSet):
        """
        Set the value of the ClientID input for this choreography. ((required, string) The ID of the publisher to set the local preference for.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((required, password) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UsersPreferredLocale input for this choreography. ((required, string) The user's preferred locale (language), e.g. 'en' for English.)
        """
        def set_UsersPreferredLocale(self, value):
            InputSet._set_input(self, 'UsersPreferredLocale', value)


"""
A ResultSet with methods tailored to the values returned by the SetUsersPreferredLocale choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SetUsersPreferredLocaleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SetUsersPreferredLocaleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetUsersPreferredLocaleResultSet(response, path)
