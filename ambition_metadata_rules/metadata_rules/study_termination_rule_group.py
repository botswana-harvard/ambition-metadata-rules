from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.decorators import register
from edc_metadata.rules.predicate import P

app_label = 'ambition_subject'


@register()
class StudyTerminationConclusionCrfRuleGroup(CrfRuleGroup):

    protocol_deviation_violation = CrfRule(
        predicate=P('termination_reason', 'eq', 'included_in_error'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.protocoldeviationviolation'])

    class Meta:
        source_model = f'{app_label}.studyterminationconclusion'
        app_label = 'ambition_metadata_rules'
