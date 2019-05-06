from Models import Demand, Link
import copy
from math import ceil
from FileWrite import FileWriter


class BT:
    def __init__(self, demands):
        print("[BF] Bruteforce start")
        self.link_module = []
        self.link_wire = []
        self.res_list = []
        self.solutions = {}
        self.solution = []
        self.all = []
        self.best_loads = []
        self.cost_function = []
        self.best_solutions = []

        self.best_cost_function = float('inf')
        for i in range(0, len(demands)):
            self.solutions[i+1] = []

    def start(self, demands, links):
        print("[BF] Uruchomiono procedure BF")
        # for l in range(len(demands)):
        #     demands[l].print_demand_properties()
        for l in range(len(links)):
            links[l].print_link_properties()
        self.load_data(links)
        self.link_in_demand(demands, links)
        k = list(self.solutions.keys())
        i = 0
        for demand in demands:
            self.rec(int(demand.demand_volume), int(
                demand.demand_volume), 0, demand.number_of_demand_paths-1, [])
            self.solutions[k[i]] = copy.deepcopy(self.solution)
            del self.solution[:]
            i += 1
            print(demand.number_of_demand_paths)
        self.getAllSolutionsIter()
        self.find_write_best()
        self.write_all()
        return

    def rec(self, volume, max_volume, level, max_level, trace):
        volumes = list(range(int(volume), -1, -1))
        for i in volumes:
            t = copy.deepcopy(trace)
            t.append(i)
            if level < max_level:
                self.rec(volume-i, max_volume, level+1, max_level, t)
            elif sum(t) == max_volume:
                self.solution.append(t)

    def load_data(self, links):
        for link in links:
            self.link_module.append(int(link.link_module))
            self.link_wire.append(int(link.number_of_modules))
        print("[BF] Wczytuje dane")

    def getAllSolutionsIter(self):
        print("All solution...")
        d_keys = list(self.solutions.keys())
        print("d_keys: ", len(d_keys))
        self.all = copy.deepcopy(self.solutions[d_keys[0]])
        l = []
        i = 0
        print("all: ", len(self.all))
        for d in d_keys[1:]:
            for e in self.all:
                for u in self.solutions[d]:
                    if i == 0:
                        l.append([e] + [u])
                    else:
                        l.append(e + [u])
            del self.all[:]
            i = 1
            for e in l:
                self.all.append(e)
            del l[:]

    def find_write_best(self):
        print("[BF] Szukam najlepszego rozwiązanias")
        for s in self.all:
            loads = self.count_load(s)
            load = sum(loads)
            cfs = []
            i = 0
            for ld in loads:
                cfs.append(ceil(ld/self.link_module[i]) - self.link_wire[i])
            cf = sum(cfs)
            if self.best_cost_function > cf:
                self.best_cost_function = copy.deepcopy(cf)
                self.best_load = load
                del self.best_solutions[:]
                self.best_solutions.append(s)
                del self.best_loads[:]
                self.best_loads.append(loads)
            elif self.best_cost_function == cf:
                self.best_solutions.append(s)
                self.best_loads.append(loads)
        fw_best = FileWriter('[BF]_BEST_SOLUTION')
        for k in range(len(self.best_solutions)):
            self.write_solution(
                fw_best, self.best_loads[k], self.best_solutions[k])
        fw_best.close()
        print("[BF] Znalazlem")
        return

    

    def link_in_demand(self, demands, links):
        self.ld = dict.fromkeys(list(range(1, len(links)+1)))
        for l in range(1, len(links)+1):
            self.ld[l] = []
        for l in range(1, len(links)+1):
            j = 1
            for d in demands:
                for k in range(d.number_of_demand_paths):
                    for i in range(len(d.list_of_demand_paths[k].link_id_list)):
                        test = 0
                        if int(d.list_of_demand_paths[k].link_id_list[i]) == l:
                             # demand position
                            self.ld[l].append([j, int(k)+1])
                j += 1

            print("LD size = ", self.ld[l])
        return self.ld


    def count_load(self, all):
        load = []
        i = 0
        for l in self.ld:
            load.append(0)
            for e in self.ld[l]:
                load[-1] += all[e[0]-1][e[1]-1]
            i += 1
        return load

    def countSolutions(self):
        counter = 1
        for k in self.solutions.keys():
            counter *= len(self.solutions[k])
        print(counter)
        return counter

    def write_all(self):
        fw_all = FileWriter('[BF]_ALL_POSSIBILITY')
        i = 1
        for s in self.all:
            loads = self.count_load(s)
            cfs = []
            j = 0
            for ld in loads:
                cfs.append(ceil(ld/self.link_module[j]) - self.link_wire[j])
                j += 1
            cf = sum(cfs)
            line = 'Solution id: ' + str(i) + ' : ' + 'Link load: ' + str(sum(loads)) + ' Cost: ' \
                   + str(cf)
            fw_all.write(line)
            line = str(s)
            fw_all.write(line)
            i += 1
        fw_all.close()

    def write_solution(self, fw, loads, offspring):
        print("BEST BF solution:")
        print(str(len(self.ld)))
        i = 0
        for link in self.ld:
            line = str(link)+' '+str(loads[i])+' ' + \
                str(ceil(loads[i]/self.link_module[i]))
            print(line)
            i += 1
        print('\n')
        print(str(len(offspring)))

        for d in range(len(offspring)):
            line = str(d+1) + ' ' + str(len(offspring[d]))
            print(line)
            temp = ""
            for e in offspring[d]:
                temp += (str(e)+' ')
            print(temp)
            print(' ')
        print(' ')


def run_brute_force(demands, links):
    bt = BT(demands)
    bt.start(demands, links)
