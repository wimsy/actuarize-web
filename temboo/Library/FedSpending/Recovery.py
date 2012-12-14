# -*- coding: utf-8 -*-

###############################################################################
#
# Recovery
# Allows access to the information in the Recovery Act Recipient Reports database.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Recovery(Choreography):

    """
    Create a new instance of the Recovery Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FedSpending/Recovery')


    def new_input_set(self):
        return RecoveryInputSet()

    def _make_result_set(self, result, path):
        return RecoveryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecoveryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Recovery
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RecoveryInputSet(InputSet):
        """
        Set the value of the Activity input for this choreography. ((conditional, string) Whether or not to search by activity. (Will provide a select list if "y"). y = yes, n = no. Defaults to n if not set.)
        """
        def set_Activity(self, value):
            InputSet._set_input(self, 'Activity', value)

        """
        Set the value of the AwardAmount input for this choreography. ((conditional, string) Grants: total Federal dollars. Loans: face value of loan obligated by the Federal Agency. Contracts: total amount obligated by Federal Agency. Vendors: payment amount. Recipients:  amount of award.)
        """
        def set_AwardAmount(self, value):
            InputSet._set_input(self, 'AwardAmount', value)

        """
        Set the value of the AwardNumber input for this choreography. ((conditional, integer) Identifying number assigned by the awarding Federal Agency. e.g. federal grant number, federal contract number or federal loan number. For grants and loans, this is assigned by the prime recipient.)
        """
        def set_AwardNumber(self, value):
            InputSet._set_input(self, 'AwardNumber', value)

        """
        Set the value of the AwardType input for this choreography. ((conditional, string) Acceptable values: G = Grants only,L = Loans only, C = Contracts only.)
        """
        def set_AwardType(self, value):
            InputSet._set_input(self, 'AwardType', value)

        """
        Set the value of the AwardingAgency input for this choreography. ((conditional, string) The 4-digit code for a specific governmental awarding agency that awarded and is administering the award on behalf of the funding agency.)
        """
        def set_AwardingAgency(self, value):
            InputSet._set_input(self, 'AwardingAgency', value)

        """
        Set the value of the CFDA input for this choreography. ((conditional, string) The Catalog of Federal Domestic Number is the number associated with the published description of a Federal Assistance program in the CFDA.)
        """
        def set_CFDA(self, value):
            InputSet._set_input(self, 'CFDA', value)

        """
        Set the value of the Detail input for this choreography. ((optional, string) Controls the level of detail of the output. Acceptable values: -1 (summary), 0 (low), 1 (medium), 2 (high), and 3 (extensive). Defaults to -1. See docs for more information.)
        """
        def set_Detail(self, value):
            InputSet._set_input(self, 'Detail', value)

        """
        Set the value of the EntityDun input for this choreography. ((conditional, string) The prime recipient for the award's Dun & Bradstreet number (no vendor information).)
        """
        def set_EntityDun(self, value):
            InputSet._set_input(self, 'EntityDun', value)

        """
        Set the value of the FirstYearRange input for this choreography. ((conditional, integer) Specifies the first year in a range of years from 2000-2006; if used, must be used with LastYearRange and without FiscalYear.)
        """
        def set_FirstYearRange(self, value):
            InputSet._set_input(self, 'FirstYearRange', value)

        """
        Set the value of the FiscalYear input for this choreography. ((conditional, integer) Specifies a single year; defaults to all years.)
        """
        def set_FiscalYear(self, value):
            InputSet._set_input(self, 'FiscalYear', value)

        """
        Set the value of the FundingAgency input for this choreography. ((conditional, string) The 4-digit code for a specific governmental agency that is responsible for funding/distributing the ARRA funds to recipients.)
        """
        def set_FundingAgency(self, value):
            InputSet._set_input(self, 'FundingAgency', value)

        """
        Set the value of the FundingTAS input for this choreography. ((conditional, string) The Agency Treasury Account Symbol (TAS) that identifies the funding Program Source. The Program Source is based out of the OMB TAS list.)
        """
        def set_FundingTAS(self, value):
            InputSet._set_input(self, 'FundingTAS', value)

        """
        Set the value of the GovtContractOffice input for this choreography. ((conditional, string) The agency supplied code of the government contracting office that executed the transaction. (For prime recipients only.))
        """
        def set_GovtContractOffice(self, value):
            InputSet._set_input(self, 'GovtContractOffice', value)

        """
        Set the value of the LastYearRange input for this choreography. ((conditional, integer) Specifies the last year in a range of years; if used, must be used with FirstYearRange and without FiscalYear.)
        """
        def set_LastYearRange(self, value):
            InputSet._set_input(self, 'LastYearRange', value)

        """
        Set the value of the MaxRecords input for this choreography. ((optional, integer) Allows you to set the maximum number of records retrieved. Defaults to 100.)
        """
        def set_MaxRecords(self, value):
            InputSet._set_input(self, 'MaxRecords', value)

        """
        Set the value of the NumberOfJobs input for this choreography. ((conditional, integer) The number of Full-Time Equivalent (FTE) jobs created and retained.)
        """
        def set_NumberOfJobs(self, value):
            InputSet._set_input(self, 'NumberOfJobs', value)

        """
        Set the value of the OfficerComp input for this choreography. ((conditional, integer) Total compensation of first highly compensated officer.)
        """
        def set_OfficerComp(self, value):
            InputSet._set_input(self, 'OfficerComp', value)

        """
        Set the value of the OrderNumber input for this choreography. ((conditional, string) This is an identifying number assigned to the contract.)
        """
        def set_OrderNumber(self, value):
            InputSet._set_input(self, 'OrderNumber', value)

        """
        Set the value of the PopCity input for this choreography. ((conditional, string) The city in which work was performed.)
        """
        def set_PopCity(self, value):
            InputSet._set_input(self, 'PopCity', value)

        """
        Set the value of the PopCountry input for this choreography. ((conditional, string) The two-letter country code for the country in which work was performed.)
        """
        def set_PopCountry(self, value):
            InputSet._set_input(self, 'PopCountry', value)

        """
        Set the value of the PopDistrict input for this choreography. ((conditional, string) The Congressional District in which work was performed.)
        """
        def set_PopDistrict(self, value):
            InputSet._set_input(self, 'PopDistrict', value)

        """
        Set the value of the PopState input for this choreography. ((conditional, string) The two-letter code for the state in which in which work was performed (the "place of performance").)
        """
        def set_PopState(self, value):
            InputSet._set_input(self, 'PopState', value)

        """
        Set the value of the PopZip input for this choreography. ((conditional, integer) The ZIP code in which work was performed.)
        """
        def set_PopZip(self, value):
            InputSet._set_input(self, 'PopZip', value)

        """
        Set the value of the ProjectDescription input for this choreography. ((conditional, string) A description of the project under which the award is funded.)
        """
        def set_ProjectDescription(self, value):
            InputSet._set_input(self, 'ProjectDescription', value)

        """
        Set the value of the RecipientDistrict input for this choreography. ((conditional, string) A 4-character numeric designation for the Congressional District within which a recipient or vendor is located. (For prime recipients and sub-recipients only.))
        """
        def set_RecipientDistrict(self, value):
            InputSet._set_input(self, 'RecipientDistrict', value)

        """
        Set the value of the RecipientName input for this choreography. ((conditional, string) The name of the recipient (prime recipient, sub-recipient, or vendor); value given is used as a text search.)
        """
        def set_RecipientName(self, value):
            InputSet._set_input(self, 'RecipientName', value)

        """
        Set the value of the RecipientStateCode input for this choreography. ((conditional, string) The postal state abbreviation for the state in the recipient's address (can be for prime recipient, sub-recipient, or vendor).)
        """
        def set_RecipientStateCode(self, value):
            InputSet._set_input(self, 'RecipientStateCode', value)

        """
        Set the value of the RecipientType input for this choreography. ((conditional, string) Recipient or vendor type: p = Prime recipients only, s = Sub-recipients only, v = Vendors only.)
        """
        def set_RecipientType(self, value):
            InputSet._set_input(self, 'RecipientType', value)

        """
        Set the value of the RecipientZip input for this choreography. ((conditional, integer) The ZIP code of the recipient (prime recipient, sub-recipient, or vendor).)
        """
        def set_RecipientZip(self, value):
            InputSet._set_input(self, 'RecipientZip', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Determines the order in which records are sorted. The default value sorts by Recipient/Vendor Name. See doc for all other values.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the TextSearch input for this choreography. ((conditional, string) Full text search.)
        """
        def set_TextSearch(self, value):
            InputSet._set_input(self, 'TextSearch', value)


"""
A ResultSet with methods tailored to the values returned by the Recovery choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RecoveryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FedSpending.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RecoveryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecoveryResultSet(response, path)
