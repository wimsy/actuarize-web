# -*- coding: utf-8 -*-

###############################################################################
#
# FinalizeOAuth
# Completes the OAuth process by retrieving a Dropbox access token and token secret for a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FinalizeOAuth(Choreography):

    """
    Create a new instance of the FinalizeOAuth Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/OAuth/FinalizeOAuth')


    def new_input_set(self):
        return FinalizeOAuthInputSet()

    def _make_result_set(self, result, path):
        return FinalizeOAuthResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FinalizeOAuthChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FinalizeOAuth
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FinalizeOAuthInputSet(InputSet):
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
        Set the value of the CallbackID input for this choreography. ((required, string) The callback token returned by the InitializeOAuth Choreo. Used to retrieve the callback data after the user authorizes.)
        """
        def set_CallbackID(self, value):
            InputSet._set_input(self, 'CallbackID', value)

        """
        Set the value of the DropboxAppKey input for this choreography. ((required, string) The APP Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        def set_DropboxAppKey(self, value):
            InputSet._set_input(self, 'DropboxAppKey', value)

        """
        Set the value of the DropboxAppSecret input for this choreography. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        def set_DropboxAppSecret(self, value):
            InputSet._set_input(self, 'DropboxAppSecret', value)

        """
        Set the value of the OAuthTokenSecret input for this choreography. ((required, string) The OAuthTokenSecret returned by the InitializeOAuth Choreo.)
        """
        def set_OAuthTokenSecret(self, value):
            InputSet._set_input(self, 'OAuthTokenSecret', value)

        """
        Set the value of the Timeout input for this choreography. ((optional, integer) The amount of time (in seconds) to poll your Temboo callback URL to see if your app's user has allowed or denied the request for access. Defaults to 20. Max is 60.)
        """
        def set_Timeout(self, value):
            InputSet._set_input(self, 'Timeout', value)


"""
A ResultSet with methods tailored to the values returned by the FinalizeOAuth choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FinalizeOAuthResultSet(ResultSet):
        """
        Retrieve the value for the "AccessTokenSecret" output from this choreography execution. ((string) The Access Token Secret retrieved during the OAuth process.)
        """
        def get_AccessTokenSecret(self):
            return self._output.get('AccessTokenSecret', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((string) The Access Token retrieved during the OAuth process.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)
        """
        Retrieve the value for the "UserID" output from this choreography execution. ((integer) The Dropbox user ID associated with the access token and secret returned.)
        """
        def get_UserID(self):
            return self._output.get('UserID', None)

class FinalizeOAuthChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FinalizeOAuthResultSet(response, path)
