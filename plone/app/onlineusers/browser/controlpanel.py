import re
import datetime

from zope.interface import implements
from zope.component import getUtility
from zope.publisher.interfaces import IPublishTraverse
from plone.registry.interfaces import IRegistry

class BaseView(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.update()
        if self.request.response.getStatus() not in (301, 302):
            return self.render()
        return ''

    def update(self):
        self.errors = {}
        self.registry = getUtility(IRegistry)
        return False

    def render(self):
        return self.index()


class ControlPanel(BaseView):
    """Control panel view
    """

    implements(IPublishTraverse)

    def getKeys(self):
        portal = self.context.portal_url.getPortalObject()
        # portal_url = self.context.portal_url()
        # self.context.Prime
        session_items = list()
        session_data = portal.aq_parent.temp_folder.session_data
        for key in session_data.keys():
            session_items.append(session_data[key])
        return session_items
