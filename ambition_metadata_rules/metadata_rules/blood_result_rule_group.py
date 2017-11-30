# from edc_metadata.constants import NOT_REQUIRED, REQUIRED
# from edc_metadata_rules import CrfRule, CrfRuleGroup, register
#
# from ..predicates import Predicates
#
# app_label = 'ambition_subject'
# pc = Predicates()
#
#
# @register()
# class BloodResultCrfRuleGroup(CrfRuleGroup):
#
#     adverse_event = CrfRule(
#         predicate=pc.func_require_ae,
#         consequence=REQUIRED,
#         alternative=NOT_REQUIRED,
#         target_models=[f'{app_label}.adverseevent'])
#
#     class Meta:
#         app_label = app_label
#         source_model = f'{app_label}.bloodresult'
