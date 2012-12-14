# -*- coding: utf-8 -*-

###############################################################################
#
# GetBounces
# Retrieve a list of bounced emails, with response codes, and optional dates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBounces(Choreography):

    """
    Create a new instance of the GetBounces Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Bounces/GetBounces')


    def new_input_set(self):
        return GetBouncesInputSet()

    def _make_result_set(self, result, path):
        return GetBouncesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBouncesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBounces
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBouncesInputSet(InputSet):
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
        Set the value of the Date input for this choreography. ((optional, string) The timestamp of the Block records. Enter 1 to return a date in a MySQL timestamp format - YYYY-MM-DD HH:MM:SS)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Days input for this choreography. ((optional, integer) The number of days (greater than 0) for which block data will be retrieved.)
        """
        def set_Days(self, value):
            InputSet._set_input(self, 'Days', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) The email to search for.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, string) The end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number to limit the number of results returned.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The beginning point in the list to retrieve bounces from.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, string) The start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of bounce to search for. Choice included are: hard, or soft.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the GetBounces choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBouncesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBouncesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBouncesResultSet(response, path)
