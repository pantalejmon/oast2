# EvolutionaryAlgorithmOAST

## Main.py 
Zostawiony na implementację do odpalania programu

## Models.py - wszystkie modele do parsera i algorytmu ewolucyjnego
- Link
- Demand
- DemandPath
- Gene
- Chromosome

## Parser.py
Przed parsowaniem plik z danymi jest dzielony na 2 części według znaku podziału (**-1**)
- **get_links_list_from_file(__net_string_links)**
Zwraca listę obiektów Link
**__net_string_links** - pierwsza część pliku z danymi (do liczby -1)
- **get_demands_from_file(__net_string_demands)**
Zwraca listę obiektów Demand 
**__net_string_demands** - druga część pliku z danymi (po liczbie -1)
- **get_number_of_links(__net_string_links)** 
Zwraca liczbę Links podaną w pierwszej części pliku
- **get_number_of_demands(__net_string_demands)**
Zwraca liczbę Demands podaną w drugiej części pliku z danymi

## EvolutionaryAlgorithm.py - funkcje związane z algorytmem ewolucyjnym
- **generate_first_population(list_of_demands, population_size_int=DEFAULT_POPULATION_SIZE)** 
Generuje pierwszą populację (lista obiektów Chromosome) na podstawie listy obiektów Demand i wielkości populacji do wygenerowania
- **generate_chromosome(list_of_demands)**
Generuje pojedynczy Chromosome
Funkcja wywoływana podczas generacji pierwszej populacji w *generate_first_population()*, raczej nie będzie potrzeby używania jej ręcznie
- **mutate_chromosome(chromosome, __mutation_probability=DEFAULT_MUTATION_PROBABILITY):** 
Dokonuje mutacji na danym obiekcie Chromosome (modyfikuje ten obiekt) ze wskazanym prawdopodobieństwem
- **crossover_chromosomes(list_of_chromosomes, crossover_probability=DEFAULT_CROSSOVER_PROBABILITY)** 
Dokonuje krzyżowania z wykorzystaniem przekazanej listy obiektów Chromosome ze wskazanym prawdopodobieństwem.
Zwraca listę obiektów Chromosome zawierającą rodziców (przekazana do funkcji list_of_chromosome) oraz wygenerowanych potomków.
- **calculate_fitness()**
Funkcja powinna obliczać i zwracać fitness dla każdego z obiektów Chromosome

## net4.txt, net12_1.txt, net12_2.txt
Skopiowane pliki z danymi ze strony przedmiotu

## Nazewnictwo z wykładu (+ jedna dodatkowa nazwa - allele)
![Zrzut ekranu 2019-04-23 o 11 25 00](https://user-images.githubusercontent.com/31706606/56570450-473d4c00-65bb-11e9-9909-99b460471a70.png)
