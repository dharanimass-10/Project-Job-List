# from django.db import models
from django.db import models
from django.contrib.auth.models import User 
# from company.models import CompanyMeta, CompanyBranchInfo, CompanyDepartment
from auththentication.models import BaseModelMixin, UserAuthentication
from django.utils.timezone import now



class EmployeeDesignation(BaseModelMixin):
    name = models.CharField(max_length=220, null=True, blank=True)
    # tag = models.CharField(max_length=220, null=True, blank=True)
    # company = models.ForeignKey(CompanyMeta, on_delete=models.CASCADE, null=True, blank=True)
    # company_branch = models.ForeignKey(CompanyBranchInfo, on_delete=models.SET_NULL, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_approver = models.BooleanField(default=False)


   
    def __str__(self):
        return str(self.name) +"===" +str(self.id)
    

class UserPersonalInfo(BaseModelMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5)
    age = models.CharField(max_length=3,null=True,blank=True)
    aadhar = models.CharField(max_length=130, null=True, blank=True)
    address = models.CharField(max_length=130, null=True, blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=True)
    dob = models.DateField(auto_now=False, null=True, blank=True)
    blood_group = models.CharField(max_length=70, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, unique=False, null=True, blank=True)
    attachment_profile = models.ImageField(upload_to='employee', null=True, blank=True)
    attached_users = models.JSONField(default=[],null=True,blank=True)

    def __str__(self):
        return self.user.first_name +"==="+ self.mobile_number+"==="+str(self.id)



class JobProviderContactInfo(BaseModelMixin):
    # is_default = models.BooleanField(default=True)
    address_id = models.CharField(max_length=30, null=True, blank=True)
    address_line_01 = models.CharField(max_length=70, null=True, blank=True)
    address_line_02 = models.CharField(max_length=70, null=True, blank=True)
    mobile_number_01 = models.CharField(max_length=20, null=True, blank=True)
    mobile_number_02 = models.CharField(max_length=20, null=True, blank=True)
    communication_address = models.CharField(
        max_length=220, null=True, blank=True)
    billing_address = models.CharField(max_length=220, null=True, blank=True)
    city = models.CharField(max_length=70, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    google_place_link = models.CharField(max_length=220, null=True, blank=True)


class EmployeeDocument(BaseModelMixin):

    ocupetion = models.CharField(max_length=220, null=True, blank=True)
    photo = models.ImageField(upload_to='employee_document', null=True, blank=True)
    time_stamp = models.DateTimeField(default=now, editable=True)
