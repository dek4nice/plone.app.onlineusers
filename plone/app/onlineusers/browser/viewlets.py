from Products.CMFPlone.utils import safe_unicode
from zope.viewlet.interfaces import IViewlet
from plone.app.layout.viewlets.common import ViewletBase
# from plone.app.layout.viewlets.common import TitleViewlet
from cgi import escape
import DateTime

class OnlineUsersViewlet(ViewletBase):
    def index(self):
        request = self.context.REQUEST
        session = request.SESSION
        response = request.RESPONSE
        user = self.context.portal_membership.getAuthenticatedMember()
        dt = DateTime.DateTime(session.getCreated())
        dateformat = '%d.%m.%Y  %H:%M'
        created = dt.strftime(dateformat)
        agent = request.HTTP_USER_AGENT
        if hasattr(user , 'getUserId'):
            userid = user.getUserId()
        else:
            userid = user.getUserName()
        self.context.REQUEST.SESSION.set('plone.app.onlineusers' , {'name':userid , 'url':request.URL0 , 'date':created , 'agent':agent})
        dummy = '<!-- [%s:%s] -->\n'
        return dummy % ('plone.app.onlineusers' , '')
        # return dummy % ('OnlineUsersViewlet' , str([userid,created,agent]))

