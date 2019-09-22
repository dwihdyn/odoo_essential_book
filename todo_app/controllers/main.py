# web page building

from odoo import http

class Todo(http.Controller):

    @http.route('/todo')        #localhost:8069/todo to access this site. to make it public, change to @http.route('/todo', auth='pubic')
    def Main(self, **kwargs):
        TodoTask = http.request.env['todo.task']
        domain_todo = [('is_done','=',False)]
        tasks = TodoTask.search(domain_todo)
        return http.request.render(
            'todo_app.index_template',{'tasks': tasks})     # to summon the QWeb template ,located under views

            