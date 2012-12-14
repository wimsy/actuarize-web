# -*- coding: utf-8 -*-

###############################################################################
#
# GetTeacherStats
# Returns teacher statistics for a school, district, or state. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTeacherStats(Choreography):

    """
    Create a new instance of the GetTeacherStats Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SchoolFinder/GetTeacherStats')


    def new_input_set(self):
        return GetTeacherStatsInputSet()

    def _make_result_set(self, result, path):
        return GetTeacherStatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTeacherStatsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTeacherStats
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTeacherStatsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your School Finder API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

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
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SchoolID input for this choreography. ((conditional, string) The Education.com id of the school you want to find.)
        """
        def set_SchoolID(self, value):
            InputSet._set_input(self, 'SchoolID', value)


"""
A ResultSet with methods tailored to the values returned by the GetTeacherStats choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTeacherStatsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Education.com.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTeacherStatsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTeacherStatsResultSet(response, path)
