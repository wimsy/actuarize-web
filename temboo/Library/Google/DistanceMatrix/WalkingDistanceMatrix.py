# -*- coding: utf-8 -*-

###############################################################################
#
# WalkingDistanceMatrix
# Obtain walking distances and times for a martix of addresses and/or latitude/longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class WalkingDistanceMatrix(Choreography):

    """
    Create a new instance of the WalkingDistanceMatrix Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/DistanceMatrix/WalkingDistanceMatrix')


    def new_input_set(self):
        return WalkingDistanceMatrixInputSet()

    def _make_result_set(self, result, path):
        return WalkingDistanceMatrixResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WalkingDistanceMatrixChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the WalkingDistanceMatrix
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class WalkingDistanceMatrixInputSet(InputSet):
        """
        Set the value of the Alternatives input for this choreography. ((optional, string) If set to true, additional routes will be returned.)
        """
        def set_Alternatives(self, value):
            InputSet._set_input(self, 'Alternatives', value)

        """
        Set the value of the Destinations input for this choreography. ((required, string) Enter the address or latitude/longitude coordinates to which directions will be generated. Multiple destinations can be separated by pipes (|).  For example: Boston, MA|New Haven|40.7160,-74.0037.)
        """
        def set_Destinations(self, value):
            InputSet._set_input(self, 'Destinations', value)

        """
        Set the value of the Language input for this choreography. ((optional, string) Set the language in which to return restults.  A list of supported languages is available here: https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
        """
        def set_Language(self, value):
            InputSet._set_input(self, 'Language', value)

        """
        Set the value of the Origins input for this choreography. ((required, string) Enter the address(es) or geo-coordinates from which distance and time will be computed. Multiple destinations can be separated by pipes (|).  For example: Boston, MA|New Haven|40.7160,-74.0037.)
        """
        def set_Origins(self, value):
            InputSet._set_input(self, 'Origins', value)

        """
        Set the value of the Region input for this choreography. ((optional, string) Enter the region code for the directions, specified as a ccTLD two-character value.)
        """
        def set_Region(self, value):
            InputSet._set_input(self, 'Region', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sensor input for this choreography. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        def set_Sensor(self, value):
            InputSet._set_input(self, 'Sensor', value)

        """
        Set the value of the Units input for this choreography. ((optional, string) Specify the units to be used when displaying results.  Options include, metric, or imperial.)
        """
        def set_Units(self, value):
            InputSet._set_input(self, 'Units', value)


"""
A ResultSet with methods tailored to the values returned by the WalkingDistanceMatrix choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class WalkingDistanceMatrixResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class WalkingDistanceMatrixChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WalkingDistanceMatrixResultSet(response, path)
