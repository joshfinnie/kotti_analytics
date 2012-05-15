from pyramid.threadlocal import get_current_registry
from kotti.tests import UnitTestBase

from kms_analytics import render_analytics_widget


def settings():
    return get_current_registry().settings


class TestAnalyticsWidget(UnitTestBase):
    def test_render_widget(self):
        self.assert_(render_analytics_widget(None, None).startswith('<script'))

    def test_render_settings(self):
        html = render_analytics_widget(None, None)
        self.assert_(u"_gaq.push(['_setAccount', 'UA-1234567-8']);" not in html)
        settings()['kms_analytics.tracking_id'] = 'UA-1234567-8'
        html = render_analytics_widget(None, None)
        self.assert_(u"_gaq.push(['_setAccount', 'UA-1234567-8']);" in html)
