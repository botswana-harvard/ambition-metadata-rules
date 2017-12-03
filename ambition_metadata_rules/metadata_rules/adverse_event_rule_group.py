# from edc_metadata.constants import NOT_REQUIRED, REQUIRED
# from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P
#
# from ..predicates import Predicates
#
# app_label = 'ambition_subject'
# pc = Predicates()
#
#
# @register()
# class AdverseEventCrfRuleGroup(CrfRuleGroup):
#
#     death_report = CrfRule(
#         predicate=P('ae_grade', 'eq', 'grade_5'),
#         consequence=REQUIRED,
#         alternative=NOT_REQUIRED,
#         target_models=[f'{app_label}.deathreport'])
#
#     recurrence_symptom = CrfRule(
#         predicate=pc.func_require_recurrence,
#         consequence=REQUIRED,
#         alternative=NOT_REQUIRED,
#         target_models=[f'{app_label}.recurrencesymptom'])
#
#     class Meta:
#         app_label = app_label
#         source_model = f'{app_label}.adverseevent'
