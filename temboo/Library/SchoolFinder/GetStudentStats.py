# -*- coding: utf-8 -*-

###############################################################################
#
# GetStudentStats
# Returns student statistics for a single school, city, or state. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetStudentStats(Choreography):

    """
    Create a new instance of the GetStudentStats Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SchoolFinder/GetStudentStats')


    def new_input_set(self):
        return GetStudentStatsInputSet()

    def _make_result_set(self, result, path):
        return GetStudentStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetStudentStatsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetStudentStats
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetStudentStatsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your School Finder API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the City input for this choreography. ((optional, string) The name of a city. Please note cities composed of two words should be formatted with a plus sign e.g. “san+Francisco.” City requests must also be accompanied by the corresponding state parameter.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the DistrictID input for this choreography. ((conditional, string) The education.com district id.)
        """
        def set_DistrictID(self, value):
            InputSet._set_input(self, 'DistrictID', value)

        """
        Set the value of the DistrictLEA input for this choreography. ((conditional, string) The LEA id of the district.)
        """
        def set_DistrictLEA(self, value):
            InputSet._set_input(self, 'DistrictLEA', value)

        """
        Set the value of the NCES input for this choreography. ((conditional, string) The National Center for Education Statistics (NCES) id of the school.)
        """
        def set_NCES(self, value):
            InputSet._set_input(self, 'NCES', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((conditional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SchoolID input for this choreography. ((conditional, string) The Education.com id of the school you want to find.)
        """
        def set_SchoolID(self, value):
            InputSet._set_input(self, 'SchoolID', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Zip input for this choreography. ((optional, integer) A five digit US postal code.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the GetStudentStats choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetStudentStatsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Education.com.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetStudentStatsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetStudentStatsResultSet(response, path)
