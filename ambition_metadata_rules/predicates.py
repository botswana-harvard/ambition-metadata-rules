from ambition_visit_schedule import DAY1
from dateutil.relativedelta import relativedelta
from edc_constants.constants import YES
from edc_metadata_rules import PredicateCollection


class Predicates(PredicateCollection):

    app_label = 'ambition_subject'
    visit_model = f'{app_label}.subjectvisit'

    def check_gt_3_months(self, visit=None, panel_name=None):
        values = self.exists(
            reference_name=f'{self.app_label}.patienthistory',
            subject_identifier=visit.subject_identifier,
            report_datetime=visit.report_datetime,
            field_name=panel_name)
        return ((visit.report_datetime - relativedelta(months=3)).date() >
                (values[0] or (visit.report_datetime).date()))

    def blood_result_abnormal(self, visit=None):
        values = self.exists(
            reference_name=f'{self.app_label}.bloodresult',
            subject_identifier=visit.subject_identifier,
            report_datetime=visit.report_datetime,
            field_name='abnormal_results_in_ae_range')
        return values[0] == YES

    def cause_of_death(self, visit=None, cause=None):
        values = self.exists(
            reference_name=f'{self.app_label}.deathreporttmg1',
            subject_identifier=visit.subject_identifier,
            report_datetime=visit.report_datetime,
            field_name='cause_of_death')
        return not (values[0] == cause)

    def model_field_exists(self, visit=None, model_lower=None, model_field=None):
        values = self.exists(
            reference_name=f'{self.app_label}.{model_lower}',
            subject_identifier=visit.subject_identifier,
            report_datetime=visit.report_datetime,
            field_name=f'{model_field}')
        return (values[0] == YES)

    def func_require_cd4(self, visit, **kwargs):
        values = self.exists(
            reference_name=f'{self.app_label}.prnmodel',
            subject_identifier=visit.subject_identifier,
            report_datetime=visit.report_datetime,
            field_name='cd4')
        if YES in values:
            return True
        elif visit.visit_code == DAY1:
            return self.check_gt_3_months(
                visit=visit, panel_name='cd4_date')
        return False

    def func_require_vl(self, visit, **kwargs):
        values = self.exists(
            reference_name=f'{self.app_label}.prnmodel',
            subject_identifier=visit.subject_identifier,
            report_datetime=visit.report_datetime,
            field_name='viral_load')
        if YES in values:
            return True
        if visit.visit_code == DAY1:
            return self.check_gt_3_months(
                visit=visit, panel_name='viral_load_date')
        return False
