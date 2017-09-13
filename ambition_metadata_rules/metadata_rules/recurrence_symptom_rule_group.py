from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P

app_label = 'ambition_subject'


@register()
class RecurrenceSymptomCrfRuleGroup(CrfRuleGroup):

    adverse_event = CrfRule(
        predicate=P('patient_readmitted', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.adverseevent'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.recurrencesymptom'
