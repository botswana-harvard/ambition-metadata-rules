from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.decorators import register
from edc_metadata.rules.predicate import P

app_label = 'ambition_subject'


@register()
class AdverseEventCrfRuleGroup(CrfRuleGroup):

    death_report = CrfRule(
        predicate=P('ae_severity_grade', 'eq', 'grade_5'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['deathreport'])

    class Meta:
        app_label = 'ambition_metadata_rules'
        source_model = f'{app_label}.adverseevent'
