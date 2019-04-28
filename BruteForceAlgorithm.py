from Models import Demand, Link
import copy
from math import ceil

class BT:
    def __init__(self, demands):
        print("Brute force starts...")
        self.link_lambda = []
        self.link_fibre = []
        self.res_list = []
        self.solutions = {}
        self.solution = []
        self.population = []
        self.best_loads = []
        self.cost_function = []
        self.best_solutions = []
        self.best_cost_function = float('inf')
        for i in range(0,len(demands)):
            self.solutions[i+1] = []
    def start(self,demands, links):
        print("[BF] Uruchomiono procedure BT")
        self.get_lambda_fibres(links)
        self.link_in_demand(demands, links)
        k = list(self.solutions.keys())
        i = 0
        for demand in demands:
            self.partial(int(demand.demand_volume),int(demand.demand_volume), 0, demand.number_of_demand_paths, [])
            self.solutions[k[i]] = copy.deepcopy(self.solution)
            print("[BF] Sprawdzam zapotrzebowanie: ", demand.start_node, demand.end_node)
            del self.solution[:]
            i += 1
        self.getAllSolutionsIter()
        self.find_write_best()
        ##self.write_all()
        return

    def partial(self, volume, max_volume, level, max_level, trace):
        volumes = list(range(int(volume), -1, -1))

        for i in volumes:
            t = copy.deepcopy(trace)
            t.append(i)
            if level < max_level:
                self.partial(volume-i, max_volume, level+1, max_level,t)
            elif sum(t) == max_volume:
                self.solution.append(t)

    def get_lambda_fibres(self, links):
        for link in links:
            self.link_lambda.append(int(link.link_module))
            self.link_fibre.append(int(link.number_of_modules))
            print("[BF] Wczytuje dane")

    def getAllSolutionsIter(self):
        print("[BF] Sprawdzam rozwiazania")
        d_keys = list(self.solutions.keys())
        self.population = copy.deepcopy(self.solutions[d_keys[0]])
        l = []
        i = 0
        for d in d_keys[1:]:
            print("[BF] d = ", d)
            for e in self.population:
                for u in self.solutions[d]:
                    if i == 0:
                        l.append([e] + [u])
                    else:
                        l.append(e + [u])
            print("[BF] Jestem dalej")
            del self.population[:]
            i = 1
            for e in l:
                self.population.append(e)
            del l[:]

    def find_write_best(self):
        print("[BF] Szukam najlepszego rozwiązanias")
        for s in self.population:
            loads = self.count_load(s)
            load = sum(loads)
            cfs = []
            i = 0
            for ld in loads:
                cfs.append(ceil(ld/self.link_lambda[i]) - self.link_fibre[i])
            cf = sum(cfs)
            print("[BF] load = ", load, " s = ", s)
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
        print("[BF] Znalazlem")
        return


    def count_load(self, population):
        """Oblicza obciazenie kazdego lacza dla podanej populacji"""
        load = []
        i = 0
        for l in self.ld:
            load.append(0)
            for e in self.ld[l]:
                load[-1] += population[e[0]-1][e[1]-1]
            i += 1
        return load

    def link_in_demand(self, demands, links):
        """ Tworzenie slownika   wystepowan krawedzi w sciezkach zapotrzebowan"""
        self.ld = dict.fromkeys(list(range(1, len(links)+1)))
        for l in range(1, len(links)+1):
            self.ld[l] = []
        for l in range(1, len(links)+1):
            j = 1
            for d in demands:
                for k in range(d.number_of_demand_paths):
                    for i in range(len(d.list_of_demand_paths[k].link_id_list)):
                        test =0
                        if int(d.list_of_demand_paths[k].link_id_list[i]) == l:
                        #     # demand position
                         self.ld[l].append([j, int(k)])
                j += 1
        return self.ld

    def printSolutions(self):
        print('Solution n [demand(path[i]) for i in len(paths)]')
        for k in list(self.solutions.keys()):
            print('demand ',k)
            i = 1
            for s in self.solutions[k]:
                print('Solution ',i,': ',s)
                i +=1
            print('-------')
        return

    def countSolutions(self):
        counter = 1
        for k in self.solutions.keys():
            counter *= len(self.solutions[k])
        print(counter)
        return counter






def run_brute_force(demands, links):
    bt = BT(demands)
    bt.start(demands,links)