from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import P, CrfRule, CrfRuleGroup, register

app_label = 'ambition_subject'


@register()
class StudyTerminationConclusionCrfRuleGroup(CrfRuleGroup):

    protocol_deviation_violation = CrfRule(
        predicate=P('termination_reason', 'eq', 'included_in_error'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.protocoldeviationviolation'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.studyterminationconclusion'
