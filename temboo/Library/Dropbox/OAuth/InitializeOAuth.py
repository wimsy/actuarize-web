# -*- coding: utf-8 -*-

###############################################################################
#
# InitializeOAuth
# Generates an authorization URL that an application can use to complete the first step in the OAuth process.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class InitializeOAuth(Choreography):

    """
    Create a new instance of the InitializeOAuth Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/OAuth/InitializeOAuth')


    def new_input_set(self):
        return InitializeOAuthInputSet()

    def _make_result_set(self, result, path):
        return InitializeOAuthResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InitializeOAuthChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the InitializeOAuth
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class InitializeOAuthInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((required, string) Your Temboo account name.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the AppKeyName input for this choreography. ((required, string) The name of your Temboo application key.)
        """
        def set_AppKeyName(self, value):
            InputSet._set_input(self, 'AppKeyName', value)

        """
        Set the value of the AppKeyValue input for this choreography. ((required, string) Your Temboo application key.)
        """
        def set_AppKeyValue(self, value):
            InputSet._set_input(self, 'AppKeyValue', value)

        """
        Set the value of the DropboxAppKey input for this choreography. ((required, string) The APP Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        def set_DropboxAppKey(self, value):
            InputSet._set_input(self, 'DropboxAppKey', value)

        """
        Set the value of the DropboxAppSecret input for this choreography. ((required, string) The AppSecret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        def set_DropboxAppSecret(self, value):
            InputSet._set_input(self, 'DropboxAppSecret', value)

        """
        Set the value of the ForwardingURL input for this choreography. ((optional, string) The URL that Temboo will redirect your users to after they grant your application access.)
        """
        def set_ForwardingURL(self, value):
            InputSet._set_input(self, 'ForwardingURL', value)


"""
A ResultSet with methods tailored to the values returned by the InitializeOAuth choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class InitializeOAuthResultSet(ResultSet):
        """
        Retrieve the value for the "AuthorizationURL" output from this choreography execution. ((string) The authorization URL that the application's user needs to go to in order to grant access to your application.)
        """
        def get_AuthorizationURL(self):
            return self._output.get('AuthorizationURL', None)
        """
        Retrieve the value for the "CallbackID" output from this choreography execution. ((string) An ID used to retrieve the callback data that Temboo stores once your application's user authorizes.)
        """
        def get_CallbackID(self):
            return self._output.get('CallbackID', None)
        """
        Retrieve the value for the "OAuthTokenSecret" output from this choreography execution. ((string) The temporary OAuth Token Secret that can be exchanged for a final token secret using the FinalizeOAuth Choreo.)
        """
        def get_OAuthTokenSecret(self):
            return self._output.get('OAuthTokenSecret', None)

class InitializeOAuthChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InitializeOAuthResultSet(response, path)
