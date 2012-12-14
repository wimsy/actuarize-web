# -*- coding: utf-8 -*-

###############################################################################
#
# SearchFilesAndFolders
# Allows you to search Dropbox for files or folders by a keyword search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchFilesAndFolders(Choreography):

    """
    Create a new instance of the SearchFilesAndFolders Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/SearchFilesAndFolders')


    def new_input_set(self):
        return SearchFilesAndFoldersInputSet()

    def _make_result_set(self, result, path):
        return SearchFilesAndFoldersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchFilesAndFoldersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchFilesAndFolders
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchFilesAndFoldersInputSet(InputSet):
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
        Set the value of the AppKey input for this choreography. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        def set_AppKey(self, value):
            InputSet._set_input(self, 'AppKey', value)

        """
        Set the value of the AppSecret input for this choreography. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        def set_AppSecret(self, value):
            InputSet._set_input(self, 'AppSecret', value)

        """
        Set the value of the FileLimit input for this choreography. ((optional, integer) Dropbox will not return a list that exceeds this specified limit. Defaults to 10,000.)
        """
        def set_FileLimit(self, value):
            InputSet._set_input(self, 'FileLimit', value)

        """
        Set the value of the Path input for this choreography. ((optional, string) The path to the folder you want to search from (i.e. RootFolder/SubFolder). Leave blank to search ALL.)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Query input for this choreography. ((required, string) The search string. Must be at least three characters long.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Root input for this choreography. ((conditional, string) The root relative to which path is specified. Valid values are "sandbox" and "dropbox" (the default). When your access token has the App folder level of access, this should be set to "sandbox".)
        """
        def set_Root(self, value):
            InputSet._set_input(self, 'Root', value)


"""
A ResultSet with methods tailored to the values returned by the SearchFilesAndFolders choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchFilesAndFoldersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchFilesAndFoldersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchFilesAndFoldersResultSet(response, path)
