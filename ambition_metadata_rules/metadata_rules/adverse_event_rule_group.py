from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P

app_label = 'ambition_subject'


@register()
class AdverseEventCrfRuleGroup(CrfRuleGroup):

    death_report = CrfRule(
        predicate=P('ae_severity_grade', 'eq', 'grade_5'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.deathreport'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.adverseevent'
