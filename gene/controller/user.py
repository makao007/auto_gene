#encoding:utf-8
import datetime

import web

from model.admin import user as m_user
from lib.utils import render, user_login, admin_login

session = web.config._session

def check (xid, other_cond={}):
    cond = {}
    cond['id'] = xid

    if other_cond:
        cond.update (other_cond)

    if not m_user.exists (**cond):
        return False

    return True

def get_user ():
    return session.get('user_id')

def default_error ():
    raise web.notfound()

class user_list:
    
    @admin_login
    def GET(self):
        request = web.input()
        index  = request.get('index',  '0').strip()
        length = request.get('length', '10') .strip()
        assert (str(index).isdigit())
        assert (str(length).isdigit())
        
        cond = {}
        cond['create_user_id'] = get_user()
        
        fields = ['uid', 'code', 'name', 'role', 'dept', 'id', 'create_user_id', 'update_user_id', 'create_date', 'update_date']
        
        for field in fields :
            if request.get(field,''):
                cond[field] = request.get(field).strip()
        
        data_list = m_user.get_many (index, length, **cond)
        
        data = {}
        data["user_id"]   = session.user_id
        data["user_name"] = session.user_name
        data["records"]   = data_list
        
        return render ('admin/user_list.html', data=data)


class user_read:
    @admin_login
    def GET(self, xid):
        assert (str(xid).isdigit())
        if check (xid):
            print 'try to read an unauthrithm data, %s record id:%s , user id:%s'  %  ('user',xid, get_user())
            raise web.notfound()
        
        data = {}
        data['record'] = m_user.get_one ({"key":"id", "value": int(xid)})
        return render ('admin/user_read.html', data = data)
        

class user_edit:
    @admin_login
    def GET(self,xid):
        assert (str(xid).isdigit())
        
        xid  = int(xid)
        data = {}
        if not xid:
            #add 
            pass
        elif not check (xid):
            print 'try to edit an unauthrithm data, table %s, id:%s , user id:%s'  %  ('user',xid, get_user())
            raise web.notfound()
        else:
            data['record'] = m_user.get_one ({"key":"id", "value": int(xid)})
            if not data['record']:
                print 'Error, try to edit record but not found data, table:%s,  id:%s'   % ('user', xid)
                raise web.notfound()
        return render ('admin/user_edit.html', data = data)
        

    @admin_login
    def POST(self):
        request = web.input()
        xid = request.get('xid','0')
        assert(str(xid).isdigit())
        xid = int(xid)
        
        if xid!=0 and not check (xid):
            print 'try to save an unauthrithm data, %s record id:%s , user id:%s'  %  ('user',xid, get_user())
            raise web.notfound()
        
        data = {}
        data['id'] = xid
        if xid==0:   #new record
            data['create_date'] = datetime.datetime.now()
            data['create_user_id'] = get_user()
        else:
            data['update_date'] = datetime.datetime.now()
            data['update_user_id'] = get_user()
        fields = ['uid', 'code', 'name', 'role', 'dept', 'id', 'create_user_id', 'update_user_id', 'create_date', 'update_date']
        for field in fields:
            data[field] = request.get(field,'')
        
        #if xid=0 then add   ;  otherwise  update
        m_user.upsert (**data)
        return web.seeother('/admin/user')


class user_delete:

    @admin_login
    def GET(self, xid):
        assert (str(xid).isdigit())
        if not check (xid):
            print 'try to delete an unauthrithm data, %s record id:%s , user id:%s'  %  ('user',xid, get_user())
            raise web.notfound()
        m_user.delete ({"id":xid})
        return web.seeother('/admin/user')
        