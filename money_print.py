from pybars import Compiler
compiler=Compiler()

TEMPLATE = "templates/reports/example.fodt"

class RenderMoney():
    def __init__(self, model, template=None):
        self.model=model
        if template is None:
            template=TEMPLATE
        self.template = template
        self.parsed = None
    def render(self, template=None):
        if template is None:
            template = self.template

        if not self.parsed:
            i=open(template,"r")
            template_str=i.read()
            i.close()
            self.parsed = compiler.compile(template_str)
        print (self.parsed)
        return self.parsed({"model":self.model})
    def render_to(self, filename, template=None):
        answer = self.render(template=template)
        o=open(filename, "w")
        o.write(answer)
        o.close()
        return True


