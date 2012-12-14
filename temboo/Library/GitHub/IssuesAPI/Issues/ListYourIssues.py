# -*- coding: utf-8 -*-

###############################################################################
#
# ListYourIssues
# Lists all issues associated with the provided access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListYourIssues(Choreography):

    """
    Create a new instance of the ListYourIssues Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/IssuesAPI/Issues/ListYourIssues')


    def new_input_set(self):
        return ListYourIssuesInputSet()

    def _make_result_set(self, result, path):
        return ListYourIssuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListYourIssuesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListYourIssues
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListYourIssuesInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Direction input for this choreography. ((optional, string) The direction of the sort order. Valid values are: asc or desc (the default).)
        """
        def set_Direction(self, value):
            InputSet._set_input(self, 'Direction', value)

        """
        Set the value of the Filter input for this choreography. ((optional, string) Filters issues using one of the following strings: assigned (the default), created, mentioned, subscribed.)
        """
        def set_Filter(self, value):
            InputSet._set_input(self, 'Filter', value)

        """
        Set the value of the Labels input for this choreography. ((optional, string) A comma separated list of label names (i.e. bug, ui, etc).)
        """
        def set_Labels(self, value):
            InputSet._set_input(self, 'Labels', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Since input for this choreography. ((optional, date) A timestamp in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Returns issues since this date.)
        """
        def set_Since(self, value):
            InputSet._set_input(self, 'Since', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Indicates how the issues will be sorted in the response. Valid sort options are: created (the default), updated, comments.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Returns issues with a particular state: open (the default) or closed.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)


"""
A ResultSet with methods tailored to the values returned by the ListYourIssues choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListYourIssuesResultSet(ResultSet):
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

class ListYourIssuesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListYourIssuesResultSet(response, path)
