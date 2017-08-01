from dateutil.relativedelta import relativedelta

from edc_metadata.rules import PredicateCollection
from edc_registration.models import RegisteredSubject

from ambition_subject.models import PatientHistory


class Predicates(PredicateCollection):

    app_label = 'ambition_subject'
    visit_model = 'ambition_subject.subjectvisit'

    def check_vl_cd4_date_gt_3_months(self, visit, panel_name):
        panel_required = False
        obj = PatientHistory.objects.get(subject_visit=visit)
        if obj.panel_name:
            if ((visit.report_datetime - relativedelta(months=3)).date() >
                    obj.panel_name):
                panel_required = True
        return panel_required

    def func_require_cd4(self, visit, **kwargs):
        return self.check_vl_cd4_date_gt_3_months(visit, 'cd4_date')

    def func_require_vl(self, visit, **kwargs):
        return self.check_vl_cd4_date_gt_3_months(visit, 'viral_load_date')
