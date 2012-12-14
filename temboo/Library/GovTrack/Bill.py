# -*- coding: utf-8 -*-

###############################################################################
#
# Bill
# Retrieves bills and resolutions in the U.S. Congress since 1973 (the 93rd Congress).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Bill(Choreography):

    """
    Create a new instance of the Bill Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Bill')


    def new_input_set(self):
        return BillInputSet()

    def _make_result_set(self, result, path):
        return BillResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BillChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Bill
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class BillInputSet(InputSet):
        """
        Set the value of the BillID input for this choreography. ((optional, integer) Specify the ID number of the bill to return only the record for that bill.)
        """
        def set_BillID(self, value):
            InputSet._set_input(self, 'BillID', value)

        """
        Set the value of the BillType input for this choreography. ((optional, string) The bill's type. See documentation for acceptable bill types.)
        """
        def set_BillType(self, value):
            InputSet._set_input(self, 'BillType', value)

        """
        Set the value of the Congress input for this choreography. ((optional, integer) The number of the congress in which the bill was introduced. The current congress is 112.)
        """
        def set_Congress(self, value):
            InputSet._set_input(self, 'Congress', value)

        """
        Set the value of the CurrentStatusDate input for this choreography. ((optional, string) The date of the last major action on the bill corresponding to the CurrentStatus (in YYYY-MM-DD format).)
        """
        def set_CurrentStatusDate(self, value):
            InputSet._set_input(self, 'CurrentStatusDate', value)

        """
        Set the value of the CurrentStatus input for this choreography. ((optional, string) The current status of the bill. See documentation for acceptable inputs.)
        """
        def set_CurrentStatus(self, value):
            InputSet._set_input(self, 'CurrentStatus', value)

        """
        Set the value of the IntroducedDate input for this choreography. ((optional, string) The date the bill was introduced (in YYYY-MM-DD format).)
        """
        def set_IntroducedDate(self, value):
            InputSet._set_input(self, 'IntroducedDate', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Number input for this choreography. ((optional, integer) The bill's number (just the integer part).)
        """
        def set_Number(self, value):
            InputSet._set_input(self, 'Number', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) You can order the results using fieldname (ascending) or -fieldname (descending) where "fieldname" is one of these values: current_status_date, introduced_date, senate_floor_schedule_postdate.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SchedulePostdate input for this choreography. ((optional, string) The date on which the bill was posted on the Senate Floor Schedule which is different from the date it was expected to be debated (in YYYY-MM-DD format).)
        """
        def set_SchedulePostdate(self, value):
            InputSet._set_input(self, 'SchedulePostdate', value)

        """
        Set the value of the Sponsor input for this choreography. ((optional, integer) The ID of the sponsor of the bill.)
        """
        def set_Sponsor(self, value):
            InputSet._set_input(self, 'Sponsor', value)


"""
A ResultSet with methods tailored to the values returned by the Bill choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class BillResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The resopnse from GovTrack.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class BillChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BillResultSet(response, path)
