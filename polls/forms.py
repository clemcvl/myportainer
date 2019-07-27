from django import forms
import docker


class NameForm(forms.Form):

    form_obj = {}
    your_name = forms.CharField(label='Your name2', max_length=100)

class Docker(forms.Form):


    def __init__(self, *args, **kwargs):

        client = docker.from_env()
        containers = client.containers.list()
        containers_active = client.containers.list(all=False)
        form_obj = {}

        #extra = kwargs.pop('extra')
        super(Docker, self).__init__(*args, **kwargs)

        #for i, question in enumerate(extra):
        #    self.fields['custom_%s' % i] = forms.CharField(label=question)

        for container in containers:
            if container in containers_active:
                checked = True
            else:
                checked = False
            print('la')
            print(container)
            self.fields[container.name] = forms.BooleanField()
    #your_name = forms.CharField(label='Your name', max_length=100)
        #form_obj[container] = forms.CheckboxInput(check_test=checked)
