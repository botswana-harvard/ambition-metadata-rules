from dateutil.relativedelta import relativedelta

from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import RequisitionRule, RequisitionRuleGroup
from edc_metadata.rules.decorators import register

from ambition_labs.labs import viral_load_panel, cd4_panel

from ..predicates import Predicates

pc = Predicates()

app_label = 'ambition_subject'


@register()
class ViralloadCD4RequisitionRuleGroup(RequisitionRuleGroup):

    require_cd4 = RequisitionRule(
        predicate=pc.func_require_cd4,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[cd4_panel])

    require_vl = RequisitionRule(
        predicate=pc.func_require_vl,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[viral_load_panel])

    class Meta:
        app_label = 'ambition_metadata_rules'
        source_model = f'{app_label}.patienthistory'
        requisition_model = f'{app_label}.subjectrequisition'