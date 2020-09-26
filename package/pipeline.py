
class pipeline:
    def pipleine_choice(ip):
        if ip==1:
            pipeline.create_new_pipeline()


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
