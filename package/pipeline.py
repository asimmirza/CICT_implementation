import os
import subprocess
import datetime
from os import path

class pipeline:
    def pipleine_choice(ip):
        if ip==1:
            pipeline.create_new_pipeline()
        elif ip==3:
            pipeline.run_pipeline()


    def create_new_pipeline():
        print("========Pipeline Creation Process Intiated=========")
        print("Pipeline name format : username-process_name-proc_date")
        print("Example : spainul-redemption-20200927")
        print("please do not use special chanracter or space in name except(-)")
        pp_name = input("Please Enter the pipeline name:")

        msg = "Need to add the object in pipeline : " + pp_name + ", in below format"
        print(msg)
        print("<team_hlq>/<sandbox_name>/{mp/run}/object_name")
        o = 1
        obj_list = []
        while True:
            msg = "Please enter the " + str(o) + " object location else enter STOP :\n"
            obj = input(msg)
            if obj == "STOP":
                break
            else:
                obj_list.append(obj)
                o= o + 1

        print("\n Below are object added : \n")
        for i in obj_list:
            print(i)

        pipeline.write_list(obj_list,pp_name)


    def write_list(obj_list,pp_name):

        fl_name = pp_name + ".pip"
        with open(fl_name, 'w') as f:
            for item in obj_list:
                f.write("%s\n" % item)


    def run_pipeline():
        print("========Pipeline Process Run Intaited =========")
        pp_name = input("Please enter the pipeline name: \n")
        obj_dtl = []

        print(pp_name)
        file_avail = pipeline.check_file_present(pp_name)
        if file_avail != True:
            print("Given Pipleline is not present")
        else:
            #Read file and convert it to list
            pp_content = pipeline.read_file(pp_name)
            for obj in pp_content:
                obj_ver = pipeline.check_version(obj)
                temp_obj_dtl = obj.replace('\n','') + "|" + obj_ver
                obj_dtl.append(temp_obj_dtl)

            #Check promoted object
            print(obj_dtl)
            username = pipeline.get_username()
            # username = "asim"
            for obj in obj_dtl:
                 o = obj.split("|")
                 check_in_date = datetime.datetime.strptime(o[1],'%Y-%m-%d')
                 print(check_in_date)
                 current_date = datetime.datetime.now() #.strftime('%Y-%m-%d')
                 print(current_date)
                 diff = current_date - check_in_date
                 print(diff.days)
                 if username==o[2] and diff.days < 2:
                    print("Obj Checkout Intiated")



    def check_file_present(file_location):
        return path.exists(file_location)

    def read_file(file_location):
        pp_file = open(file_location,'r')
        pp_content = pp_file.readlines()
        print(pp_content)
        return pp_content

    def check_version(obj_name):
        # cmd = 'export AB_AIR_ROOT='
        # result = subprocess.check_output(cmd, shell=True)
        # cmd = 'air object versions <eme_location> | tail -1 | awk '{print $2"|"$4}''
        # result = subprocess.check_output(cmd, shell=True)
        return "2020-05-11|asim"

    def get_username():
        username = subprocess.check_output("whoami",shell=True)
        return username.decode("ascii")

    def checkout(obj_location,eme):
        # cmd = 'export AB_AIR_ROOT='
        # result = subprocess.check_output(cmd, shell=True)
        # cmd = 'air project export <>' + '-basedir <>' + '-files'
        pass
