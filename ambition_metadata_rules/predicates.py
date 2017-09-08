from dateutil.relativedelta import relativedelta

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

    def func_require_cd4(self, visit, **kwargs):
        if visit.visit_code == '1000':
            return self.check_gt_3_months(visit=visit, panel_name='cd4_date')
        return False

    def func_require_vl(self, visit, **kwargs):
        if visit.visit_code == '1000':
            return self.check_gt_3_months(visit=visit, panel_name='viral_load_date')
        return False
