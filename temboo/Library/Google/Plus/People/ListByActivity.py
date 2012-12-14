# -*- coding: utf-8 -*-

###############################################################################
#
# ListByActivity
#  Returns all of the people in the specified collection for a particular activity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListByActivity(Choreography):

    """
    Create a new instance of the ListByActivity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Plus/People/ListByActivity')


    def new_input_set(self):
        return ListByActivityInputSet()

    def _make_result_set(self, result, path):
        return ListByActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListByActivityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListByActivity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListByActivityInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ActivityID input for this choreography. ((required, string) The ID of the activity to get the list of people for. ActiviyIDs can be retrieved by running the Google.Plus.Activities.Search Choreo.)
        """
        def set_ActivityID(self, value):
            InputSet._set_input(self, 'ActivityID', value)

        """
        Set the value of the Callback input for this choreography. ((optional, string) Specifies a JavaScript function that will be passed the response data for using the API with JSONP.)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the ClientID input for this choreography. ((required, string) The client ID provided by Google when you register your application.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((required, string) The client secret provided by Google when you registered your application.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the Collection input for this choreography. ((required, string) Valid values are: "plusoners" (lists all people who have +1'd this activity) and "resharers" (lists all people who have reshared this activity).)
        """
        def set_Collection(self, value):
            InputSet._set_input(self, 'Collection', value)

        """
        Set the value of the Fields input for this choreography. ((optional, string) Used to specify fields to include in a partial response. This can be used to reduce the amount of data returned. See documentation for syntax rules.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) The maximum number of people to include in the response. Used for paging through results. Valid values are: 1 to 20. Default is 10.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the PageToken input for this choreography. ((optional, string) The "NextPageToken" returned in the Choreo output. Used to page through large result sets.)
        """
        def set_PageToken(self, value):
            InputSet._set_input(self, 'PageToken', value)

        """
        Set the value of the PrettyPrint input for this choreography. ((optional, boolean) A flag used to pretty print the json response to make it more readable. Defaults to "true".)
        """
        def set_PrettyPrint(self, value):
            InputSet._set_input(self, 'PrettyPrint', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the UserIP input for this choreography. ((optional, string) Identifies the IP address of the end user for whom the API call is being made. Used to enforce per-user quotas.)
        """
        def set_UserIP(self, value):
            InputSet._set_input(self, 'UserIP', value)


"""
A ResultSet with methods tailored to the values returned by the ListByActivity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListByActivityResultSet(ResultSet):
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListByActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListByActivityResultSet(response, path)
