from dateutil.relativedelta import relativedelta

from edc_metadata_rules import PredicateCollection


class Predicates(PredicateCollection):

    app_label = 'ambition_subject'
    visit_model = f'{app_label}.subjectvisit'

    def check_vl_cd4_date_gt_3_months(self, visit, panel_name):
        values = self.exists(
            model='patienthistory',
            subject_identifier=visit.subject_identifier,
            report_datetime=visit.report_datetime,
            field_name=panel_name)
        return ((visit.report_datetime - relativedelta(months=3)).date() >
                (values[0] or (visit.report_datetime).date()))

    def func_require_cd4(self, visit, **kwargs):
        return self.check_vl_cd4_date_gt_3_months(visit, 'cd4_date')

    def func_require_vl(self, visit, **kwargs):
        return self.check_vl_cd4_date_gt_3_months(visit, 'viral_load_date')
