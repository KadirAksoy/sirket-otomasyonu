from numpy import choose


class Label():
    def __init__(self,label_name) :
        self.label_name= label_name
        self.work = True         #Sınırsız döngüye girmesi için 

    def application(self):
        chose = self.menu()

        if chose == 1 :
            self.worker_add()

        elif chose == 2 :
            self.worker_remove()
        
        elif chose == 3 :
            self.show_salary()

    def menu(self):
        chose = int(input("Welcome to {} \n 1-)worker_add \n2 2-)worker_remove \n3 3-)show_salary ".format(self.label_name)))
        while chose < 1 or chose > 4 :
            chose = int(input("Please choose 1 to 3 "))
        return chose
                

    def worker_add(self):
        id=1
        name = input("Please enter name:")
        lastname = input("Please enter lastname:")
        salary = input("Please enter salary:")
        gender = input("Please enter gender")

        with open("calisan.txt","a+") as worker_folder:
            worker_list = worker_folder.readlines()

        if len(worker_list == 0):
            id = 1 
        else :
            with open("calisanlar.txt","r") as worker_folder :
                id = int(worker_folder.readlines()[-1].split(")")[0])+ 1

        with open("calisan.txt","a+") as worker_folder:
            worker_folder.write("{}){}-{}-{}-{}\n".format(id,name,lastname,gender,salary))
    
    def worker_remove(self):
        with open("calisan.txt","r") as worker_folder:
            worker = worker_folder.readlines()
        tworker_list = []

        for i in worker :
                tworker_list.append(" ".join(i[:-1].split(")")))

        worker_choose = int(input("Enter the number of the employee you want to remove:"))

        while worker_choose < 1 or worker_choose > len(tworker_list):
            worker_choose = int(input("Please enter the number of the employe you want to remove 1-{}").format(len(tworker_list)))

        worker.pop(worker_choose-1)

        max_number = len(worker)

        nworker_list = []

        count = 1 

        for i in worker:
            nworker_list.append(str(count) + ")" + i.split(")")[1])
            count += 1 

        with open("calisan.txt","w") as worker_folder :
            worker_folder.write(nworker_list)

    #def show_salary(self):
        #with open("calisan.txt","r") as worker_folder :
            #worker_salary_list = worker_folder.readlines()
            
            



