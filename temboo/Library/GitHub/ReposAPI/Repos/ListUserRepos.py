# -*- coding: utf-8 -*-

###############################################################################
#
# ListUserRepos
# Retrieves a list of public repositories for the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListUserRepos(Choreography):

    """
    Create a new instance of the ListUserRepos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Repos/ListUserRepos')


    def new_input_set(self):
        return ListUserReposInputSet()

    def _make_result_set(self, result, path):
        return ListUserReposResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUserReposChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListUserRepos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListUserReposInputSet(InputSet):
        """
        Set the value of the Direction input for this choreography. ((optional, string) Valid values are asc or desc. Default behavior is desc unless sorting by full_name in which case, the direction is asc.)
        """
        def set_Direction(self, value):
            InputSet._set_input(self, 'Direction', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) The sort order of the results. Valid values are: created, updated, pushed, or full_name (the default).)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of repos to return. Valid values are: all (the default), owner, public, or member.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the User input for this choreography. ((required, string) The GitHub username.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the ListUserRepos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListUserReposResultSet(ResultSet):
        """
        Retrieve the value for the "LastPage" output from this choreography execution. ((integer) If multiple pages are available for the response, this contains the last available page.)
        """
        def get_LastPage(self):
            return self._output.get('LastPage', None)
        """
        Retrieve the value for the "Limit" output from this choreography execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        def get_Limit(self):
            return self._output.get('Limit', None)
        """
        Retrieve the value for the "NextPage" output from this choreography execution. ((integer) If multiple pages are available for the response, this contains the next page that you should retrieve.)
        """
        def get_NextPage(self):
            return self._output.get('NextPage', None)
        """
        Retrieve the value for the "Remaining" output from this choreography execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        def get_Remaining(self):
            return self._output.get('Remaining', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from GitHub.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListUserReposChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListUserReposResultSet(response, path)
