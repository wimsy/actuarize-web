# -*- coding: utf-8 -*-

###############################################################################
#
# RecordActivity
# Records a newly-completed background activity, or begins recording an activity still in progress.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RecordActivity(Choreography):

    """
    Create a new instance of the RecordActivity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/BackgroundActivities/RecordActivity')


    def new_input_set(self):
        return RecordActivityInputSet()

    def _make_result_set(self, result, path):
        return RecordActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecordActivityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RecordActivity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RecordActivityInputSet(InputSet):
        """
        Set the value of the Activity input for this choreography. ((required, json) A JSON string containing the key/value pairs for the activity to create. See documentation for formatting examples.)
        """
        def set_Activity(self, value):
            InputSet._set_input(self, 'Activity', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the RecordActivity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RecordActivityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) Contains the string 'true" when a new activity is created successfully.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "URI" output from this choreography execution. ((string) The activity uri that was created.)
        """
        def get_URI(self):
            return self._output.get('URI', None)

class RecordActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecordActivityResultSet(response, path)
