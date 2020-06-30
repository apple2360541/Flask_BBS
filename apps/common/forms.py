from apps.cms.forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp, input_required
import hashlib


class SMSCaptachaForm(BaseForm):
    salt = 'dqgeryeu5sdg56sdg486575es#$%'
    telephone = StringField(validators=[regexp(r'1[3456789]\d{9}')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[input_required()])

    def validate(self):
        result = super(SMSCaptachaForm, self).validate()
        if not result:
            return False
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        # md5函数要传一个bytes类型的字符串
        sign2 = hashlib.md5((timestamp + telephone + self.salt).encode("utf-8")).hexdigest()
        print(sign)
        print(sign2)
        return sign == sign2
