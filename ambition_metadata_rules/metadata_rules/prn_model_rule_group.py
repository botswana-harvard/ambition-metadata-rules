from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule, CrfRuleGroup, P
from edc_metadata.rules.decorators import register


app_label = 'ambition_subject'


@register()
class PrnModelCrfRuleGroup(CrfRuleGroup):

    adverse_event = CrfRule(
        predicate=P('adverse_event', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.adverseevent'])

    adverse_event_tmg = CrfRule(
        predicate=P('adverse_event_tmg', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.adverseeventtmg'])

    adverse_event_followup = CrfRule(
        predicate=P('adverse_event_followup', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.adverseeventfollowup'])

    blood_result = CrfRule(
        predicate=P('blood_result', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.bloodresult'])

    microbiology = CrfRule(
        predicate=P('microbiology', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.microbiology'])

    radiology = CrfRule(
        predicate=P('radiology', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.radiology'])

    recurrence_symptom = CrfRule(
        predicate=P('recurrence_symptom', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.recurrencesymptom'])

    protocol_deviation = CrfRule(
        predicate=P('protocol_deviation', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.protocoldeviationviolation'])

    lumbar_puncture = CrfRule(
        predicate=P('lumbar_puncture', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.lumbarpuncturecsf'])

    death_report = CrfRule(
        predicate=P('death_report', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.deathreport'])

    death_report_tmg1 = CrfRule(
        predicate=P('death_report_tmg1', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.deathreporttmg1'])

    death_report_tmg2 = CrfRule(
        predicate=P('death_report_tmg2', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.deathreporttmg2'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.prnmodel'
