from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register
from ..predicates import Predicates

pc = Predicates()
app_label = 'ambition_subject'


@register()
class DeathReportCrfRuleGroup(CrfRuleGroup):

    death_report = CrfRule(
        predicate=pc.func_require_death_report_tmg1,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.deathreporttmg1'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.deathreport'


@register()
class DeathReportTmgCrfRuleGroup(CrfRuleGroup):

    death_report = CrfRule(
        predicate=pc.func_require_death_report_tmg2,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.deathreporttmg2'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.deathreporttmg1'
