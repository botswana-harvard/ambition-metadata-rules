from ambition_visit_schedule import DAY1, DAY3, DAY5
from arrow.arrow import Arrow
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from django.test import TestCase
from django.test.utils import override_settings
from edc_reference import LongitudinalRefset
from edc_reference.tests import ReferenceTestHelper

from ..predicates import Predicates


class TestPredicates(TestCase):

    reference_helper_cls = ReferenceTestHelper
    visit_model = 'ambition_subject.subjectvisit'
    reference_model = 'edc_reference.reference'
    app_label = 'ambition_subject'

    def setUp(self):

        Site.objects.create(name='gaborone', id=10, domain='bw.testing.com')
        Site.objects.create(name='harare', id=20, domain='zw.testing.com')
        Site.objects.create(name='blantyre', id=30, domain='mw.testing.com')

        self.subject_identifier = '111111111'
        self.reference_helper = self.reference_helper_cls(
            visit_model=self.visit_model,
            subject_identifier=self.subject_identifier)

        report_datetime = Arrow.fromdatetime(
            datetime(2017, 7, 7)).datetime
        self.reference_helper.create_visit(
            report_datetime=report_datetime, timepoint=DAY1)
        self.reference_helper.create_visit(
            report_datetime=report_datetime + relativedelta(days=3),
            timepoint=DAY3)
        self.reference_helper.create_visit(
            report_datetime=report_datetime + relativedelta(days=5),
            timepoint=DAY5)

    @property
    def subject_visits(self):
        return LongitudinalRefset(
            subject_identifier=self.subject_identifier,
            visit_model=self.visit_model,
            name=self.visit_model,
            reference_model_cls=self.reference_model
        ).order_by('report_datetime')

    def test_cd4_requisition_required(self):
        pc = Predicates()
        self.reference_helper.create_for_model(
            report_datetime=self.subject_visits[0].report_datetime,
            reference_name=f'{self.app_label}.patienthistory',
            visit_code=self.subject_visits[0].visit_code,
            cd4_date=(self.subject_visits[0].report_datetime - relativedelta(months=4)).date())
        self.assertTrue(pc.func_require_cd4(self.subject_visits[0]))

    def test_cd4_requisition_not_required(self):
        pc = Predicates()
        self.reference_helper.create_for_model(
            report_datetime=self.subject_visits[0].report_datetime,
            reference_name=f'{self.app_label}.patienthistory',
            visit_code=self.subject_visits[0].visit_code,
            cd4_date=(self.subject_visits[0].report_datetime).date())
        self.assertFalse(pc.func_require_cd4(self.subject_visits[0]))

    def test_vl_requisition_required(self):
        pc = Predicates()
        self.reference_helper.create_for_model(
            report_datetime=self.subject_visits[0].report_datetime,
            reference_name=f'{self.app_label}.patienthistory',
            visit_code=self.subject_visits[0].visit_code,
            viral_load_date=(
                self.subject_visits[0].report_datetime - relativedelta(months=4)).date())
        self.assertTrue(pc.func_require_vl(self.subject_visits[0]))

    def test_vl_requisition_not_required(self):
        pc = Predicates()
        self.reference_helper.create_for_model(
            report_datetime=self.subject_visits[0].report_datetime,
            reference_name=f'{self.app_label}.patienthistory',
            visit_code=self.subject_visits[0].visit_code,
            viral_load_date=(self.subject_visits[0].report_datetime).date())
        self.assertFalse(pc.func_require_vl(self.subject_visits[0]))

    @override_settings(SITE_ID=30)
    def test_pkpd_site_eq_blantyre(self):
        pc = Predicates()
        self.assertTrue(pc.func_require_pkpd_stopcm(self.subject_visits[0]))

    @override_settings(SITE_ID=20)
    def test_pkpd_site_eq_harare(self):
        pc = Predicates()
        self.assertFalse(pc.func_require_pkpd_stopcm(self.subject_visits[0]))

    @override_settings(SITE_ID=10)
    def test_qpcr_requisition_site_eq_gaborone(self):
        pc = Predicates()
        self.assertTrue(
            pc.func_require_qpcr_requisition(self.subject_visits[0]))

    @override_settings(SITE_ID=20)
    def test_qpcr_requisition_site_eq_harare(self):
        pc = Predicates()
        self.assertFalse(
            pc.func_require_qpcr_requisition(self.subject_visits[0]))
